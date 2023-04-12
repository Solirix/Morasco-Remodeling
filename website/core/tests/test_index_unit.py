from django.test import TestCase
import requests

class portfolio_page_tests(TestCase):
    
    def test_images_loading(self):
        response = self.client.get('/index/')
        self.assertContains(response, 'core/images/Squared/about-us-pic(1)"')

    def test_about_us_section(self):
        response = self.client.get('/index/')
        self.assertContains(response, 'class="slanted-text-container"')