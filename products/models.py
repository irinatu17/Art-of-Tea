from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ImageGallery(models.Model):

    class Meta:
        verbose_name_plural = 'Image Galleries'

    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):


    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image_gallery = models.ForeignKey('ImageGallery', null=True, blank=True,
                                      on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    # Fields related to teas and teaware
    has_weight = models.BooleanField(default=False, null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True)
    is_a_service = models.BooleanField(default=False)
    # Fields related to services/tea ceremonies
    itinerary = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.name

