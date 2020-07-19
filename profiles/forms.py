from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'profile_full_name': 'Full Name',
            'profile_phone_number': 'Phone Number',
            'profile_postcode': 'Postcode',
            'profile_town_or_city': 'Town/City',
            'profile_address_line1': 'Address Line 1',
            'profile_address_line2': 'Address Line 2',
            'profile_county': 'County/State',
        }

        for field in self.fields:
            if field != 'profile_country':
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
