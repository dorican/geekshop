"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.urls import path, re_path
# import mainapp.views as mainapp
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),

    re_path(r'^shop/$', mainapp.shop, name='shop'),
    re_path(r'^shop/page/(?P<page>\d+)/$', mainapp.shop, name='shop_paginator'),

    re_path(r'^product/(?P<slug>[-\w]+)/$', mainapp.product, name='product'),

    re_path(r'^category/(?P<slug>[-\w]+)/$', mainapp.category, name='category'),
    re_path(r'^category/(?P<slug>[-\w]+)/page/(?P<page>\d+)/$', mainapp.category, name='category_paginator'),
    re_path(r'^search/$', mainapp.search, name='search'),
    # re_path(r'^search/$', mainapp.SearchView.as_view(), name='search'),

]
