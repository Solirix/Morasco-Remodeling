from django.test import TestCase
from selenium import webdriver
import requests

class ImageTestCase(TestCase):
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
