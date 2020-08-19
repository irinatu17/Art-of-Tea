from django.shortcuts import render
from .models import Event


def events(request):
    """
    A view to return events page, getting event items(day,time and description)
    from the Event model
    """
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/events.html', context)
