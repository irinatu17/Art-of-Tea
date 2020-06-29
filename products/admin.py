from django.contrib import admin
from .models import Product, Category, ImageGallery, Itinerary, ItineraryItem


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


class ItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'service',
    )


class ItineraryItemAdmin(admin.ModelAdmin):
    list_display = (
        'itinerary',
        'time',
        'text',
    )


class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_url',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(ItineraryItem, ItineraryItemAdmin)
