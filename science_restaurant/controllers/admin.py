from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


class VisitorAdmin(admin.ModelAdmin):
    # list_display = ('id', 'nik_name', 'about', 'time_create', 'photo', 'is_published')
    list_display = ('id', 'nik_name', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'nik_name')     # Link for edit
    search_fields = ('title', 'about')          # Search fields
    list_editable = ('is_published',)           # filter edit
    list_filter = ('is_published', 'time_create')   # Filter table
    prepopulated_fields = {'slug': ('nik_name', )}
    # fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo',
    #           'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True  # Верхняя панель

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Visitor, VisitorAdmin)

admin.site.site_title = 'Science restaurant'
admin.site.site_header = 'Админ-панель сайта Science restaurant'