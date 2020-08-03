from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, ItineraryItem, Itinerary
from .forms import ProductForm


def all_products(request):
    """ A view to display all of the products with search queries"""

    products = Product.objects.filter(is_a_service=False)

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
    all_products = Product.objects.filter(is_a_service=False)
    product = get_object_or_404(all_products, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def services(request):
    """ A view to display all of the services"""
    services = Product.objects.filter(is_a_service=True)
    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)


def service_details(request, service_id):
    """ A view to display single service details page """
    all_services = Product.objects.filter(is_a_service=True)
    service = get_object_or_404(all_services, pk=service_id)
    itinerary = Itinerary.objects.get(service=service)
    itinerary_items = ItineraryItem.objects.filter(itinerary=itinerary)

    context = {
        'service': service,
        'itinerary': itinerary,
        'itinerary_items':  itinerary_items,
    }
    return render(request, 'products/service_details.html', context)


def add_product(request):
    """ A view allowing admin to add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. \
                            Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
