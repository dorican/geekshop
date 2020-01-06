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
from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^$', adminapp.ShopUserListView.as_view(), name='index'),

    re_path(r'^shopuser/create/$', adminapp.shopuser_create, name='shopuser_create'),
    re_path(r'^shopuser/update/(?P<pk>\d+)/$', adminapp.shopuser_update, name='shopuser_update'),
    re_path(r'^shopuser/delete/(?P<pk>\d+)/$', adminapp.shopuser_delete, name='shopuser_delete'),

    re_path(r'^productcategory/list/$', adminapp.productcategory_list, name='productcategory_list'),

    # re_path(r'^productcategory/create/$', adminapp.productcategory_create, name='productcategory_create'),
    re_path(r'^productcategory/create/$', adminapp.ProductCategoryCreateView.as_view(), name='productcategory_create'),

    # re_path(r'^productcategory/update/(?P<pk>\d+)/$', adminapp.productcategory_update, name='productcategory_update'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(),
            name='productcategory_update'),

    # re_path(r'^productcategory/delete/(?P<pk>\d+)/$', adminapp.productcategory_delete, name='productcategory_delete'),
    re_path(r'^productcategory/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='productcategory_delete'),

    re_path(r'^productcategory/products/(?P<pk>\d+)/$', adminapp.productcategory_products,
            name='productcategory_products'),

    re_path(r'^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),

    # re_path(r'^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    re_path(r'^product/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
]
