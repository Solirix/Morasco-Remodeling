import time
from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager # this line and the next can be changed to use other browsers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestUI(LiveServerTestCase):
    def test_image_address_perry(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/Squared/about-us-pic(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_ladder(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/random/output-onlinepngtools.png'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_tools(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/random/result.png'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_saws(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/random/result(1).png'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_bannerelec(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/normal_sized/heated_floor.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_bannerbase(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/after/bradley-basement-after.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_bannerdeck(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/Squared/IMG_20180509_162146(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_bannerbath(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/Squared/PXL_20210908_193124241(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_carouselthree(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/normal_sized/PXL_20210908_193124241(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_carouseltwo(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/normal_sized/IMG_20180509_162146(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')
    def test_image_address_carouselone(self):
        
        url = 'http://127.0.0.1:8000/static/core/images/normal_sized/IMG_20161109_152215(1).jpg'
        response = requests.get(url)
        if response.status_code == 200:
            print('Image loaded successfully!')
        else:
            print('Image failed to load.')

    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000") # Replace with your website URL
    
    def test_image_presence(self):
        images = self.driver.find_elements_by_tag_name('img')
        for image in images:
            self.assertTrue(image.is_displayed())
    
    def test_image_source(self):
        expected_sources = [
            '/static/core/images/normal_sized/IMG_20161109_152215(1).jpg',
            '/static/core/images/normal_sized/IMG_20180509_162146(1).jpg',
            '/static/core/images/normal_sized/PXL_20210908_193124241(1).jpg',
            '/static/core/images/Squared/PXL_20210908_193124241(1).jpg',
            '/static/core/images/Squared/IMG_20180509_162146(1).jpg',
            '/static/core/images/after/bradley-basement-after.jpg',
            '/static/core/images/normal_sized/heated_floor.jpg',
            '/static/core/images/Squared/about-us-pic(1).jpg',
            '/static/core/images/random/output-onlinepngtools.png',
            '/static/core/images/random/result.png'
            '/static/core/images/random/result(1).png',
            
        ]
        images = self.driver.find_elements_by_tag_name('img')
        for i, image in enumerate(images):
            source = image.get_attribute('src')
            self.assertIn(expected_sources[i], source)
            
    def tearDown(self):
        self.driver.quit()
class MyUITestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def test_contact_us_button(self):
        self.driver.get('http://localhost:8000')
        contact_button = self.driver.find_element_by_class_name('contact_us_button')
        contact_button.click()
        self.assertIn('Contact Us', self.driver.title)
    
    def tearDown(self):
        self.driver.quit()