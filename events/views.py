from django.shortcuts import render
from .models import Event


# Create your views here.
def events(request):
    """
    A view to return events page
    """
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/events.html', context)
