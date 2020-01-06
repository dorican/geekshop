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
from django.contrib import admin
from django.urls import path, re_path, include

import mainapp.views as mainapp

urlpatterns = [
    re_path(r'^', include('mainapp.urls', namespace='main')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^myadmin/', include('adminapp.urls', namespace='myadmin')),
    re_path(r'^callback/', include('callbackapp.urls', namespace='callback')),
    re_path(r'^news/', include('newsapp.urls', namespace='news')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),

    re_path(r'^', include('social_django.urls', namespace='social')),
    path('summernote/', include('django_summernote.urls')),

    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
