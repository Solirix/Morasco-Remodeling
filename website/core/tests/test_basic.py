from django.test import TestCase

# Create your tests here. 

# To run the enitre tests directory use: ./manage.py test core.tests
# To run a specific test file use: ./manage.py test core.tests.test_name (without the .py extension)
# DO NOT USE FORWARD SLASHES OR LIFE WILL BE PAINFUL
# WHEN MAKING A NEW TEST FILE USE test_ AS THE PREFIX OR IT WILL NOT BE RECOGNIZED AS A TEST FILE

class BasicTests(TestCase):
    # this will send a request to the home page
    def test_home_page_status_code(self):
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page_status_code(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    # this will check if the index.html template is used
    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/index.html')

    def test_portfolio_page_template(self):
        response = self.client.get('/portfolio/')
        self.assertTemplateUsed(response, 'core/portfolio.html')

    def test_contact_page_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'core/contact.html')