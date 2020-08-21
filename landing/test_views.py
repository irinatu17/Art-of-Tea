from django.test import TestCase

class TestLandingViews(TestCase):

    def test_get_landing_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing/includes/benifits_section.html")
        self.assertTemplateUsed(response, "landing/includes/hero_img_and_buttons.html")
        self.assertTemplateUsed(response, "landing/includes/landing_about.html")
        self.assertTemplateUsed(response, "landing/includes/landing_contact.html")
        self.assertTemplateUsed(response, "landing/includes/landing_events.html")
        self.assertTemplateUsed(response, "landing/includes/landing_reviews.html")
        self.assertTemplateUsed(response, "landing/includes/quote_section.html")
        self.assertTemplateUsed(response, "landing/includes/tea_ceremony_section.html")
        self.assertTemplateUsed(response, "landing/includes/tea_shop_section.html")
