from django.contrib import admin
from .models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'category',)
    # search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'price', 'quantity',)
    list_display_links = ('name',)
    search_fields = ('name', 'price', 'quantity',)

    class Meta:
        model = Product


admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
admin.site.register(Product, ProductAdmin)



