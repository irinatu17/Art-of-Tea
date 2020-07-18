from django.shortcuts import render, get_object_or_404

from .models import Profile
from .forms import ProfileForm


def profile(request):
    """ A view to display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'profile_form': profile_form,
        'orders': orders,
    }
    template = 'profiles/profile.html'

    return render(request, template, context)
