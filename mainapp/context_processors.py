from basketapp.models import Basket
from .models import ProductCategory


def basket(request):
    # print(f'context processor work')
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return {
        'basket': basket,
    }


def products_menu(request):
    products_menu = ProductCategory.objects.all().exclude(is_active=False).order_by('name')
    return {
        'products_menu': products_menu,
    }
