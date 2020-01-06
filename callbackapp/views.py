from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from callbackapp.forms import CallbackForm
from mainapp.models import Product


def callback(request):
    data = dict()
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            email_data = form.save()
            # data['form_is_valid'] = True
            # products = []
            # data['products_html'] = render_to_string('callbackapp/list.html', {'products': products})
            subject = 'Заявка с сайта'
            message = 'Имя: {}\nНомер телефона: {}'.format(email_data.name, email_data.phone)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
        else:
            data['form_html'] = render_to_string('callbackapp/modal_window.html', {'form': form}, request=request)
    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('callbackapp/modal_window.html', {'form': CallbackForm()}, request=request)

    return JsonResponse(data)
