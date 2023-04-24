from django.test import TestCase
from selenium import webdriver
import requests

class contact_us_page_tests(TestCase):

    def test_contact_us_hero(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="hero"')

    def test_contact_us_alerts(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="alert"') 

    def test_contact_us_input(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="input-group"')
        self.assertContains(response, 'id="email"')
        self.assertContains(response, 'id="message"')
        self.assertContains(response, 'id="number"')
        self.assertContains(response, 'id="name"')

    def test_contact_us_button(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="button"') 

    def test_contact_us_rows(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'class="row"')