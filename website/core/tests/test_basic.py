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
    
    def test_services_page_status_code(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
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

    def test_services_page_template(self):
        response = self.client.get('/services/')
        self.assertTemplateUsed(response, 'core/services.html')

    def test_about_page_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'core/about.html')

    # this will make sure the logo is using the proper link to the home page
    def test_logo_link(self):
        response = self.client.get('/')
        self.assertContains(response, '<meta charset="utf-8">', html=True)
        self.assertContains(response, '<meta name="viewport" content="width=device-width, initial-scale=1.0">', html=True)
        self.assertContains(response, '<nav class ="py-6 px-6 flex justify-between items-center border-b border-gray-200">', html=True)
        self.assertContains(response, '<div class="pr-20" id="logo-home-page">', html=True)
        self.assertContains(response, '<a href="/">', html=True)
        self.assertContains(response, '<img src="core/images/mr_logo.png" width="250">', html=True)
    