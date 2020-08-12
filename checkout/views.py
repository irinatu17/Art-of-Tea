from django.shortcuts import render, redirect, \
    reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import OrderItemDetails, Order
from products.models import Product
from profiles.models import Profile
from profiles.forms import ProfileForm

from cart.contexts import cart_contents

import stripe
import json


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'comment': request.POST['comment'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderItemDetails(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for datetime, quantity in item_data['items_by_datetime'].items():
                            order_line_item = OrderItemDetails(
                                order=order,
                                product=product,
                                quantity=quantity,
                                datetime=datetime,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart\
                         wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            if request.POST['save_info'] == "true":
                request.session['save_info'] = True
            else:
                request.session['save_info'] = False
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check again your information.')
    else:
        if not cart:
            messages.error(request, "There's nothing in your\
                 cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.profile_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.profile_phone_number,
                    'country': profile.profile_country,
                    'postcode': profile.profile_postcode,
                    'town_or_city': profile.profile_town_or_city,
                    'address_line1': profile.profile_address_line1,
                    'address_line2': profile.profile_address_line2,
                    'county': profile.profile_county,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.error(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'profile_full_name': order.full_name,
                'profile_phone_number': order.phone_number,
                'profile_country': order.country,
                'profile_postcode': order.postcode,
                'profile_town_or_city': order.town_or_city,
                'profile_address_line1': order.address_line1,
                'profile_address_line2': order.address_line2,
                'profile_county': order.county,
            }
            user_profile_form = ProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@require_POST
def cache_checkout_data(request):
    """
    A view to store user's input for the checkbox "save-info" field
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'comment': request.POST.get('comment'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
