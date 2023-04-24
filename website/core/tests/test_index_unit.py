from django.test import TestCase
from selenium import webdriver
import requests

class index_page_tests(TestCase):
    
    def test_images_loading(self):
        response = self.client.get('/')
        self.assertContains(response, 'core/images/Squared/about-us-pic(1).jpg')

    def test_about_us_section(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="slanted-text-container"')

    def test_about_us_class(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="daddy-perry"')

    def test_services_banner_css_classes(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="banner-container"')
        self.assertContains(response, 'class="banner-item"')
        self.assertContains(response, 'class="banner-text"')
        self.assertContains(response, 'class="text-center"')

    def test_services_banner_images(self):
        response = self.client.get('/')
        self.assertContains(response, 'core/images/Squared/PXL_20210908_193124241(1).jpg')
        self.assertContains(response, 'core/images/Squared/IMG_20180509_162146(1).jpg')
        self.assertContains(response, 'core/images/after/bradley-basement-after.jpg')
        self.assertContains(response, 'core/images/normal_sized/heated_floor.jpg')

    def test_inline_css_services_banner(self):
        response = self.client.get('/')
        self.assertContains(response, 'style="display: flex; justify-content: center; align-items: center;"')
        self.assertContains(response, 'style="font-size: 2rem !important;"')
        self.assertContains(response, 'class="flex justify-center items-center h-full mt-5"')
        