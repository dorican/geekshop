from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# class NewsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title', 'author', 'created',)
#     list_display_links = ('title',)
#     search_fields = ('title', 'author',)
#
#     class Meta:
#         model = News


class NewsAdminText(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created',)
    list_display_links = ('title',)
    search_fields = ('title', 'author',)
    summernote_fields = ('content',)

    class Meta:
        model = News


# admin.site.register(News, NewsAdmin)
admin.site.register(News, NewsAdminText)