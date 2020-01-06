from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import *
from django.contrib import auth
from django.conf import settings
from django.db import transaction


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else None
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                next = request.POST['next'] if 'next' in request.POST.keys() else None
                # print(f'next: {next}')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index') if not next else next)
    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'личный кабинет',
        'form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                # print(f'Сообщение для подтверждения регистрации отправлено')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                # print(f'Ошибка отправки сообщение для подтверждения регистрации')
                return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = ShopUserRegisterForm()
    context = {
        'page_title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


@transaction.atomic
def update(request):
    if request.method == 'POST':
        edit_form = ShopUserUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        edit_form = ShopUserUpdateForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'page_title': 'редактирование профиля',
        'edit_form': edit_form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/update.html', context)


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key])
    title = 'Подтверждение учетной записи {}'.format(user.username)
    message = 'Для подтверждения учетной записи {} на портале перейдите по ссылке: {}{}'.format(user.username, settings.DOMAIN_NAME, verify_link)
    print = 'from: {}, to: {}'.format(settings.EMAIL_HOST_USER, user.email)
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print('user {} is activated'.format(user))
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {
                'page_title': 'подтверждение регистрации',
            }
            return render(request, 'authapp/verification.html', context)
        else:
            print('error activation user: {}'.format(user))
            context = {
                'page_title': 'подтверждение регистрации',
            }
            return render(request, 'authapp/verification.html', context)
    except Exception as e:
        print('error activation user: {}'.format(e.args))
    return HttpResponseRedirect(reverse('main:index'))