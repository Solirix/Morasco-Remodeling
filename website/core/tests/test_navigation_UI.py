# pip install selenium, webdriver-manager

import time
from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager # this line and the next can be changed to use other browsers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestUI(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.driver.get('http://127.0.0.1:8000/portfolio/') # call portfolio page

        assert "Portfolio" in self.driver.title # check if the title of the page is "Portfolio"

    # make sure the logo is clickable and takes you to the home page
    def test_image_link(self):
        self.driver.get('http://127.0.0.1:8000/portfolio')
        logo = self.driver.find_element(By.ID, "logo")
        time.sleep(2)
        logo.click()
        assert "Home" in self.driver.title

    # make sure the navbar links are clickable and take you to the correct page
    def test_navbar_links(self):
        self.driver.get('http://127.0.0.1:8000/')
        link = self.driver.find_element(By.ID, "service nav")
        link.click()
        time.sleep(2)
        assert "Services" in self.driver.title

        link = self.driver.find_element(By.ID, "portfolio nav")
        link.click()
        time.sleep(2)
        assert "Portfolio" in self.driver.title

        link = self.driver.find_element(By.ID, "about nav")
        link.click()
        time.sleep(2)
        assert "About" in self.driver.title

        link = self.driver.find_element(By.ID, "contact nav")
        link.click()
        time.sleep(2)
        assert "Contact" in self.driver.title

    def test_bottom_navbar_links(self):
        self.driver.get('http://127.0.0.1:8000/')
        link = self.driver.find_element(By.ID, "about bottom nav")
        link.click()
        time.sleep(2)
        assert "About" in self.driver.title

        link = self.driver.find_element(By.ID, "contact bottom nav")
        link.click()
        time.sleep(2)
        assert "Contact" in self.driver.title

        link = self.driver.find_element(By.ID, "policy bottom nav")
        link.click()
        time.sleep(2)
        assert "https://www.example.com/policy" == self.driver.current_url # this is the policy page

        link = self.driver.find_element(By.ID, "terms bottom nav")
        link.click()
        time.sleep(2)
        assert "https://www.example.com/terms" == self.driver.current_url # this is the terms page

    def test_background_services(self):
        self.driver.get('http://127.0.0.1:8000/services/')
        body_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body_class = body_element.get_attribute("class")
        assert "bg-gradient-to-b" in body_class
        assert "from-orange-100" in body_class
        assert "to-blue-200" in body_class
    def test_homepage_background(self):
        self.driver.get('http://127.0.0.1:8000/')
        body_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body_class = body_element.get_attribute("class")
        assert "bg-gradient-to-b" in body_class
        assert "from-orange-100" in body_class
        assert "to-blue-200" in body_class