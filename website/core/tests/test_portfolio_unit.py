from django.test import TestCase
import requests

class portfolio_page_tests(TestCase):

    def test_css_being_called(self):
        response = self.client.get('/portfolio/')
        self.assertContains(response, 'class="port_container"')
        self.assertContains(response, 'class="port_photos"')
        self.assertContains(response, 'class="before_and_after_heading"')
        self.assertContains(response, 'class="portfolio_text_blocks"')
        self.assertContains(response, 'class="reviews_container"')
        self.assertContains(response, 'class="reviews"')
        self.assertContains(response, 'class="signature"')