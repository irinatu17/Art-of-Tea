from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to display all of the products with search queries"""

    products = Product.objects.all()

    # empty query and categories when tha page is loaded
    query = None
    categories = None

    if request.GET:
        # allow to show thr specific categories of products
        if 'category' in request.GET:
            # to split categories into list ar the commas
            categories = request.GET['category'].split(',')
            # the __in syntax allow to search for the name field
            # in categories model
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'serach_term_input' in request.GET:
            query = request.GET['serach_term_input']
            # if the query is blank, the error message will be displayed
            if not query:
                messages.error(request,
                               "You didn't enter any search key words!\
                                    Please, try again.")
                return redirect(reverse('products'))
            # if query is not blank -> ability to search by name OR description
            search_queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            # pass quieries to the filter method to actually filter products
            products = products.filter(search_queries)

    context = {
        'products': products,
        'selected_categories': categories,
        'search_word': query,
    }
    return render(request, 'products/all_products.html', context)


def product_details(request, product_id):
    """ A view to display single product details page """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
