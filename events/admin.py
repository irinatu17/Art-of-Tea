from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'weekday',
        'time',
        'description',
    )


admin.site.register(Event, EventAdmin)
