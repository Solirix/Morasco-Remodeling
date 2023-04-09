import time
from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager # this line and the next can be changed to use other browsers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestUI(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

    def tearDown(self):
        self.driver.quit()

    def test_ask_us_button(self):
        self.driver.get('http://127.0.0.1:8000/portfolio/')
        