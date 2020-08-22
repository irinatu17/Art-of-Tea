from django.contrib import admin
from .models import Product, Category, Itinerary, ItineraryItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'has_weight',
        'image',
        'image_url',
        'discontinued',
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(ItineraryItem, ItineraryItemAdmin)
