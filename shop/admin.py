from django.contrib import admin
from . models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug':('product',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)