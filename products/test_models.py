from django.test import TestCase
from .models import Product


class TestModel(TestCase):

    def test_done_default_to_false(self):
        product = Product.objects.create(name="Test product", description="Test description",
                                         price=2.10)
        self.assertFalse(product.has_weight)
