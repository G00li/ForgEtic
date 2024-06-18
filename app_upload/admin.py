from django.contrib import admin
from .models import Folder

# Register your models here.

@admin.register(Folder)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['name', 'user']
    search_fields = ['name', 'user']
    ordering = ['name']