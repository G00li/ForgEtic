from django.contrib import admin
from .models import Folder, File

# Register your models here.

@admin.register(Folder)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['name', 'user']
    search_fields = ['name', 'user']
    ordering = ['name']

@admin.register(File)
class Files(admin.ModelAdmin):
    list_display = ['file', 'user', 'parent_folder']
    list_filter = ['file', 'user', 'parent_folder']
    search_fields = ['file', 'user', 'parent_folder']
    ordering = ['user']
