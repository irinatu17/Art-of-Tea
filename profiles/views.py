from django.shortcuts import render, get_object_or_404

from .models import Profile


def profile(request):
    """ A view to display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    context = {
        'profile': profile,
    }
    template = 'profiles/profile.html'

    return render(request, template, context)
