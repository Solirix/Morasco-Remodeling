from django.test import TestCase
import requests
import pytest

class NavigationTest(TestCase):
    # this will check if the navigation links are in use and pointing to the correct pages
    def test_nav_class_links(self):
        response = self.client.get('/')
        self.assertContains(response, 'href="/portfolio/"')
        self.assertContains(response, 'href="/services/"')
        self.assertContains(response, 'href="/about/"')
        self.assertContains(response, 'href="/contact/"')
        self.assertContains(response, 'href="/"')

    # check if the links are redirecting to the correct pages
    def test_nav_class_links_redirect(self):
        
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)

    
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
    
   
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    # This will try to navigate to the logo's image address, and if it loads it will respond with the code 200. If not, something went wrong.
    def test_image_address(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/mr_logo.png'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')

    # check if each link on the page is there
    def test_links_displaying(self):

        url = 'http://127.0.0.1:8000/about/'
        response = requests.get(url)
        if response.status_code == 200:
            print('Link exists!')
        else:
            print('Link does not exist.')

        url = 'http://127.0.0.1:8000/contact/'
        response = requests.get(url)
        if response.status_code == 200:
            print('Link exists!')
        else:
            print('Link does not exist.')

        url = 'https://www.thryv.com/client-privacy-policy/'
        response = requests.get(url)
        if response.status_code == 200:
            print('Link exists!')
        else:
            print('Link does not exist.')

        url = 'https://www.thryv.com/client-terms-of-use/'
        response = requests.get(url)
        if response.status_code == 200:
            print('Link exists!')
        else:
            print('Link does not exist.') 