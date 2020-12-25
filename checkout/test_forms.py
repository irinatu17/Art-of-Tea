from django.test import TestCase
from .forms import OrderForm

# Create your tests here.


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '123456 789',
            'address_line1': '123 test street',
            'town_or_city': 'test city',
            'country': 'RU'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
