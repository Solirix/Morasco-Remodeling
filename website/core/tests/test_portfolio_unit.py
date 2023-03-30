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
    
    def test_images_loading(self):
        response = self.client.get('/portfolio/')
        self.assertContains(response, 'core/images/before/bradley-basement-before.jpg"')
        self.assertContains(response, 'core/images/after/bradley-basement-after.jpg"')
        self.assertContains(response, 'core/images/before/glendale-bath-before.jpg"')
        self.assertContains(response, 'core/images/after/glendale-bath-after.jpg"')
        self.assertContains(response, 'core/images/before/kush-deck-before.jpg"')
        self.assertContains(response, 'core/images/after/kush-deck-after.jpg"')
        self.assertContains(response, 'core/images/before/railing-before.jpg"')
        self.assertContains(response, 'core/images/after/railing-after.jpg"')