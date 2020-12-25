from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItemDetails

"""
Signals call update_total function each time an OrderItem
is attached to the order or deleted
"""


@receiver(post_save, sender=OrderItemDetails)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on OrderItem update or create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderItemDetails)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on OrderItem delete
    """
    instance.order.update_total()
