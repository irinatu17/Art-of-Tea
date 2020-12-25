from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address_line1', 'address_line2',
                  'town_or_city', 'county', 'postcode', 'country', 'comment'
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'town_or_city': 'Town/City',
            'county': 'County/State',
            'postcode': 'Postcode',
            'country': 'Country',
            'comment': 'Additional comment/query',
        }
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            self.fields['comment'].widget.attrs['rows'] = 3
