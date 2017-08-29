from __future__ import absolute_import
from django.contrib import admin
from home.models import Product, Photo

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    inlines = [PhotoInline]


admin.site.register(Product, ProductAdmin)