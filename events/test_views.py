from django.test import TestCase

class TestEventsViews(TestCase):

    def test_get_events_page(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/includes/contact_details.html")
        self.assertTemplateUsed(response, "events/includes/events_table.html")
        self.assertTemplateUsed(response, "events/includes/main_paragraph.html")

