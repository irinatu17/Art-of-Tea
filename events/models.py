from django.db import models


class Event(models.Model):

    weekday = models.CharField(max_length=10)
    time = models.CharField(max_length=80)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.weekday
