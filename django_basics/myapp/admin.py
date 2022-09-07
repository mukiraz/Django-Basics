from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'isActive', 'slug']
    prepopulated_fields = { "slug": ("name",)}
    list_display_links = ["name", "price"]
    list_filter = ["name", "price"]
    list_editable = ["isActive"]
    search_fields = ["name","description"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
