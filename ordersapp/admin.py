from django.contrib import admin
from ordersapp.models import OrderItem, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'user', 'is_active',)

    class Meta:
        model = Order


class OrderItemAdmin(admin.ModelAdmin):

    # list_display_links = ('name',)
    # search_fields = ('name', 'price', 'quantity',)

    class Meta:
        model = OrderItem


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
