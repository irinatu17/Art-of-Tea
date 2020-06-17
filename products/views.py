from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to display all of the products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', context)


def product_details(request, product_id):
    """ A view to display single product details page """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
