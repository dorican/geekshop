import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from newsapp.models import News
from .models import *
from django.shortcuts import render_to_response


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        founded_products = Product.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q) | Q(short_desc__icontains=q)
        ).order_by('name')
        # founded_products = Product.objects.filter(
        #     Q(name__in=q) | Q(description__in=q) | Q(short_desc__in=q)
        # ).order_by('name')
        context = {
            'page_title': 'Результаты поиска',
            'founded_products': founded_products,
            'query': q,
        }
        return render_to_response('mainapp/search.html', context)
    else:
        context = {
            'page_title': 'Результаты поиска',
        }
        return render_to_response('mainapp/search.html', context)


# def search_form(request):
#     return render_to_response('mainapp/search.html')


# class SearchView(View):
#     template_name = "mainapp/search.html"
#
#     def get_result_search(self, request, *args, **kwargs):
#         query = self.request.GET.get('q')
#         founded_products = Product.objects.filter(Q(name__icontains=query))
#         context = {
#             'founded_products': founded_products,
#             'query': query,
#         }
#         return render(self.request, self.template_name, context)


# def get_products_menu():
#     return ProductCategory.objects.all().exclude(is_active=False)

# def bad_search(request):
#     # The following line will raise KeyError if 'q' hasn't
#     # been submitted!
#     message = 'You searched for: %r' % request.GET['q']
#     return HttpResponse(message)


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all().order_by('product__category')
    else:
        []


def index(request):
    all_products = Product.objects.all().order_by('?')[:6]
    all_news = News.objects.all().order_by('-created')[:4]
    context = {
        'page_title': 'РФснаб.ру - комплексное снабжение',
        'all_products': all_products,
        'all_news': all_news,
        # 'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def shop(request, slug=None, page=1):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'page_title': 'каталог',
        'all_products': products_paginator,
    }
    return render(request, 'mainapp/shop.html', context)


def category(request, slug, page=1):
    all_products = Product.objects.filter(category__slug=slug).exclude(is_active=False)
    single_category = ProductCategory.objects.filter(slug=slug)
    paginator = Paginator(all_products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'all_products': products_paginator,
        'single_category': single_category,
    }
    return render(request, "mainapp/category.html", context)


def product(request, slug):
    single_product = Product.objects.filter(slug=slug)
    same_products = Product.objects.all().filter(category__product__slug=slug).exclude(slug=slug).order_by('?')[:4]
    context = {
        'single_product': single_product,
        'same_products': same_products,
    }
    return render(request, "mainapp/product.html", context)


