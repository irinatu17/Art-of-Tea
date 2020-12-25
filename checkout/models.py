import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import Profile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=60, null=False, blank=False)
    address_line2 = models.CharField(max_length=60, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')
    comment = models.TextField(max_length=254, null=True, blank=True)

    def _generate_order_number(self):
        """
        Generates unique and permanent, random 32 characters order number
         using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total each time an order item is added,
        accounting for delivery costs.
        """
        self.order_total = self.orderitems.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItemDetails(models.Model):
    """Model displaying individual cart items details
        relating to the specific order"""

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='orderitems')
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, blank=False, editable=False)
    # Because of Django DateTimeField functionality does not support
    #  the desired format (DD/MM/YYYY HH:mm) it was decided
    #  to replace it with the CharField to achieve better UI
    datetime = models.CharField(null=True, blank=True, max_length=20)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item total
        and update the order total.
        """
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
