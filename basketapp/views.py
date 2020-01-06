from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_basket


@login_required
def index(request):
    context = {
        'page_title': 'корзина',
        'basket': get_basket(request),
    }
    return render(request, "basketapp/basket.html", context)


@login_required
def basket_add(request, slug):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product', kwargs={'slug': slug}))
    product = get_object_or_404(Product, slug=slug)
    basket_item = Basket.objects.filter(user=request.user, product=product).first()
    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_update(request, pk, quantity):
    if request.is_ajax():
        basket_obj = get_object_or_404(Basket, pk=pk)
        quantity = int(quantity)
        if quantity > 0:
            basket_obj.quantity = quantity
            basket_obj.save()
        else:
            basket_obj.delete()

        context = {
            'basket': get_basket(request),
        }
        result = render_to_string('basketapp/includes/inc__basket_list.html', context)
        return JsonResponse(
            {'result': result}
        )
