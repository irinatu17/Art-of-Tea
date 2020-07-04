from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address_line1', 'address_line2',
                  'town_or_city', 'county', 'postcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels, add asterisk to the required fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'town_or_city': 'Town or City',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country',
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
