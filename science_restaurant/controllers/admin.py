from django.contrib import admin

# Register your models here.
from .models import *


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nik_name', 'about', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'nik_name')     # Link for edit
    search_fields = ('title', 'about')          # Search fields
    list_editable = ('is_published',)           # filter edit
    list_filter = ('is_published', 'time_create')   # Filter table
    prepopulated_fields = {'slug': ('nik_name', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Visitor, VisitorAdmin)
