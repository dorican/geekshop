from django.contrib import admin
from .models import *


class ShopUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'age')
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name', 'email', 'age')

    class Meta:
        model = ShopUser


admin.site.register(ShopUser, ShopUserAdmin)
