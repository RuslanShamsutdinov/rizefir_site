from django.contrib import admin
from .models import Product, Category, Image

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'description', 'size', 'is_published')


@admin.register(Image)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'image', 'main_photo')
