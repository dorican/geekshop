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
from . import views as callbackapp

app_name = 'callbackapp'

urlpatterns = [
    re_path(r'^$', callbackapp.callback, name='index'),
    # re_path(r'^success/$', callbackapp.sent_mail, name='sent_mail'),
]
