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

    name = models.CharField(max_length=254, null=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Itinerary(models.Model):

    class Meta:
        verbose_name_plural = 'itineraries'

    name = models.CharField(max_length=254, null=True)
    service = models.OneToOneField('Product', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ItineraryItem(models.Model):

    class Meta:
        ordering = ('time', )

    itinerary = models.ForeignKey('Itinerary', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    time = models.CharField(max_length=254)
    text = models.CharField(max_length=254)

    def __str__(self):
        return self.text


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
    is_a_service = models.BooleanField(default=False)
    # Fields related to services/tea ceremonies
    duration = models.CharField(null=True, max_length=254)

    def __str__(self):
        return self.name
