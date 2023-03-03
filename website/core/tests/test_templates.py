from django.test import TestCase

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
    