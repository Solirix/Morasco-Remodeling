from django.test import TestCase

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
