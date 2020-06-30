from django.shortcuts import render


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')
