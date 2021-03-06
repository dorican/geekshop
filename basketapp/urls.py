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
from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.index, name='index'),
    re_path(r'^add/(?P<slug>[-\w]+)/', basketapp.basket_add, name='add'),
    re_path(r'^delete/(?P<pk>\d+)/', basketapp.basket_delete, name='delete'),
    re_path(r'^update/(?P<pk>\d+)/(?P<quantity>\d+)/', basketapp.basket_update, name='update'),
]
