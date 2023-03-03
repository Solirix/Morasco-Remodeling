# pip install selenium, webdriver-manager

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

    def test(self):
        self.driver.get('http://127.0.0.1:8000/portfolio/') # call portfolio page

        assert "Portfolio" in self.driver.title # check if the title of the page is "Portfolio"

    def test_image_link(self):
        self.driver.get('http://127.0.0.1:8000/portfolio')
        logo = self.driver.find_element(By.ID, "logo")
        logo.click()
        assert "Home" in self.driver.title

