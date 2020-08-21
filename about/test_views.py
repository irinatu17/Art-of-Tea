from django.test import TestCase


class TestAboutViews(TestCase):

    def test_get_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/includes/our_mission.html")
        self.assertTemplateUsed(response, "about/includes/our_principles.html")
        self.assertTemplateUsed(response, "about/includes/who_we_are.html")
