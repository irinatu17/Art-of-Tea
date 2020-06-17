from django.contrib import admin
from .models import Product, Category, ImageGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'has_weight',
        'image_gallery',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ImageGalleryAdmin(admin.ModelAdmin):
   list_display = (
        'friendly_name',
        'name',
        'image',
        'image_url',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
