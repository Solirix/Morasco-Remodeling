# this file tests the services page to make sure that the correct html and css is being rendered
# it also tests that the images are loading correctly

from django.test import TestCase

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

    def test_images_loading(self):
        response = self.client.get('/services/')
        self.assertContains(response, 'core/images/normal_sized/deck-with-seats.jpg')
        self.assertContains(response, 'core/images/normal_sized/wood-wall-basement.jpg')

