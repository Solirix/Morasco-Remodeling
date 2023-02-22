from django.test import TestCase

# Create your tests here.

# In terminal, run the following command: "python manage.py test core" with quotes, or am I lying?

class BasicTest(TestCase):
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