from django.test import TestCase
from .models import Event


class TestEventsModels(TestCase):

    def test_event_created_correctly(self):

        event1 = Event.objects.create(weekday = 'Monday',time = "14:00", description = "Tea testing")
        event2 = Event.objects.create(weekday = 'Saturday', time = "all day", description = "Yoga and Tea lection")
        event1.save()
        event2.save()
        self.assertEquals(event1.weekday, 'Monday')
        self.assertEquals(event1.time, '14:00')
        self.assertEquals(event1.description, 'Tea testing')
        self.assertEquals(event2.weekday, 'Saturday')
        self.assertEquals(event2.time, 'all day')
        self.assertEquals(event2.description, 'Yoga and Tea lection')


    
    def test__str_method_returns_weekday(self):

        event = Event.objects.create(weekday = 'Monday',time = "14:00", description = "Tea testing")

        self.assertEqual(event.__str__(), "Monday")
    
