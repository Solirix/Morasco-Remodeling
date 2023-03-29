from django.test import TestCase
import requests

class services_page_tests(TestCase):

    def test_css_being_called(self):
        response = self.client.get('/services/')
        self.assertContains(response, 'class="services_page_container"')
        self.assertContains(response, 'id="services_page_header"')
        self.assertContains(response, 'class="service_container"')
        self.assertContains(response, 'class="service_heading"')
        self.assertContains(response, 'class="service_text"')
        self.assertContains(response, 'class="didnt_see_container"')
        self.assertContains(response, 'id="didnt_see_text"')
        self.assertContains(response, 'id="ask_us_today"')
        

