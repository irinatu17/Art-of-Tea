from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'sku',
                  'category', 'price',
                  'rating', 'has_weight',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Product Name',
            'description': 'Description',
            'sku': 'SKU',
            'category': 'Category',
            'price': 'Price',
            'rating': 'Rating (0-5)',
            'has_weight': 'Product Type',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['description'].widget.attrs['rows'] = 4


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price',
                  'rating', 'duration',
                #   'is_a_service',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Service Name',
            'description': 'Description',
            'price': 'Price',
            'rating': 'Rating (0-5)',
            'duration': 'Duration (in hrs)',
            # 'is_a_service': 'is a service',

        }

        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['description'].widget.attrs['rows'] = 4
        # self.fields['is_a_service'].initial = True
        # self.fields['is_a_service'].disabled = True
        # self.fields['is_a_service'].widget.attrs['readonly'] = 'readonly'
