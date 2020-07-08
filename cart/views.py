from django.shortcuts import render, redirect, \
 reverse, HttpResponse, get_object_or_404
from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the selected product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
    # place = None
    # if 'service_place' in request.POST:
    #     place = request.POST.get('service_place')
    # comment = None
    # if 'comment' in request.POST:
    #     comment = request.POST.get('comment')
    # data_time = None
    # if 'data_time' in request.POST:
    #     data_time = request.POST.get('data_time')
    # if item_id in list(cart.keys()):
    #     cart[item_id] += quantity
    # else:
    #     cart[item_id] = quantity
    # cart = {
    # 'product': {
    #     item_id: quantity
    #     },
    # 'service': {
    #     item_id: {
    #         'place': place,
    #         'comment': comment,
    #         'data_time': data_time,
    #         }
    #     }
    # if item_id in cart:
    #     cart[item_id] = int(cart[item_id]) + quantity
    # else:
    #     cart[item_id] = cart.get(item_id, quantity)
    # cart['product'][item_id] = quantity
    # cart['service'][item_id] = {
    #     'place': place,
    #     'comment': comment,
    #     'data_time': data_time
    #     }


def update_cart(request, item_id):
    """Update the quantity of the selected product in the cart
        to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
