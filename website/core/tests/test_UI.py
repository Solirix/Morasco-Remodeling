# pip install selenium, webdriver-manager

from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager # this line and the next can be changed to use other browsers
from selenium.webdriver.chrome.service import Service as ChromeService



class TestUI(LiveServerTestCase):
    def test(self):

        # this should install the latest version of ChromeDriver and set it up to be used by Selenium
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

        driver.get('http://127.0.0.1:8000/portfolio/') # call portfolio page

        assert "Portfolio" in driver.title # check if the title of the page is "Portfolio"


