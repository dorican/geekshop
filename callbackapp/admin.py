from django.contrib import admin
from callbackapp.models import CallbackApplication


class CallbackApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'add_datetime',)
    list_display_links = ('name',)
    search_fields = ('name', 'phone',)

    class Meta:
        model = CallbackApplication


admin.site.register(CallbackApplication, CallbackApplicationAdmin)
