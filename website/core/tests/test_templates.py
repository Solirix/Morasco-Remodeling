from django.test import TestCase
import time

# Create your tests here. 

# To run the enitre tests directory use: ./manage.py test core.tests
# To run a specific test file use: ./manage.py test core.tests.test_name (without the .py extension)
# DO NOT USE FORWARD SLASHES OR LIFE WILL BE PAINFUL
# WHEN MAKING A NEW TEST FILE USE test_ AS THE PREFIX OR IT WILL NOT BE RECOGNIZED AS A TEST FILE

class TemplateTests(TestCase):

    # these will check if the correct template is being used for each page
    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/index.html')

   
        response = self.client.get('/portfolio/')
        self.assertTemplateUsed(response, 'core/portfolio.html')

    
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'core/contact.html')

    
        response = self.client.get('/services/')
        self.assertTemplateUsed(response, 'core/services.html')

    
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'core/about.html')

    # these will check if the correct background is being used for each page    
    def test_template_backgrounds(self):
        response = self.client.get('/')
        self.assertContains(response, 'body class="bg-gradient-to-b from-orange-100 to-blue-200"')

        response = self.client.get('/portfolio/')
        self.assertContains(response, 'body class="bg-gradient-to-b from-orange-100 to-blue-200"')

        response = self.client.get('/contact/')
        self.assertContains(response, 'body class="bg-gradient-to-b from-orange-100 to-blue-200"')

        response = self.client.get('/services/')
        self.assertContains(response, 'body class="bg-gradient-to-b from-orange-100 to-blue-200"')

        response = self.client.get('/about/')
        self.assertContains(response, 'body class="bg-gradient-to-b from-orange-100 to-blue-200"')
    
    # check to make sure the nav bar image is in use
    def test_navbar_image(self):
        response = self.client.get('/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="250"')

        response = self.client.get('/portfolio/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="250"')

        response = self.client.get('/contact/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="250"')

        response = self.client.get('/services/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="250"')

        response = self.client.get('/about/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="250"')


    # check to make sure the footer image is in use
    def test_footer_image(self):
        response = self.client.get('/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="300"')

        response = self.client.get('/portfolio/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="300"')

        response = self.client.get('/contact/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="300"')

        response = self.client.get('/services/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="300"')

        response = self.client.get('/about/')
        self.assertContains(response, 'img src="/static/core/images/mr_logo.png" width="300"')

    # check to make sure the correct paragraph is being used for each footer header
    def test_footer_headers(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="mt-3 mb-2 font-semibold text-gray-550">Morasco Remodeling: Create, Fix, Dream')
        self.assertContains(response, 'class="mb-2 font-semibold text-gray-550"')
        self.assertContains(response, 'class="mb-2 font-semibold text-gray-550"')