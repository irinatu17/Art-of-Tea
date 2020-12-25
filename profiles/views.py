from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ A view to display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile was successfully updated!')
        else:
            messages.error(request, 'Update failed.\
                 Please ensure the form is valid.')
    else:
        profile_form = ProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
    }
    template = 'profiles/profile.html'

    return render(request, template, context)


@login_required
def order_history(request):
    profile = get_object_or_404(Profile, user=request.user)
    orders = profile.orders.all().order_by('-purchase_date')

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_details(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
