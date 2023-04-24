from django.test import TestCase
from selenium import webdriver
import requests

class contact_us_page_tests(TestCase):

    def test_contact_us_hero(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="hero"')