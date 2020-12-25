from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Itinerary(models.Model):

    class Meta:
        verbose_name_plural = 'itineraries'

    name = models.CharField(max_length=254, null=True)
    service = models.OneToOneField('Product', null=True, blank=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItineraryItem(models.Model):

    class Meta:
        ordering = ('time', )

    itinerary = models.ForeignKey('Itinerary', null=True, blank=True,
                                  on_delete=models.CASCADE)
    time = models.CharField(max_length=254)
    text = models.CharField(max_length=254)

    def __str__(self):
        return self.text


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.01)])
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 null=True, blank=True,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    is_a_service = models.BooleanField(default=False)
    discontinued = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Fields related to only teas and teaware
    has_weight = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    # Field related to  only services(tea ceremonies)
    duration = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(24)])

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name
