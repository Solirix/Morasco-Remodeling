# This file will click every single link in both the nav bar and footer of the website and make sure that they work

import time
from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
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

    # when the nav bar tests run make sure to hide the debig toolbar as it is "on top" of the about and contact links
    # this is fine as the debug toolbar is not shown in production
    def test_navbar(self):
        self.driver.get('http://127.0.0.1:8000/')
        li_element = self.driver.find_element(By.ID, "logo")
        time.sleep(1)
        li_element.click()

        time.sleep(1)
        li_element = self.driver.find_element(By.XPATH, '//a[@href="/services/"]')
        time.sleep(1)
        li_element.click()

        time.sleep(1)
        li_element = self.driver.find_element(By.XPATH, '//a[@href="/portfolio/"]')
        time.sleep(1)
        li_element.click()

        time.sleep(2)
        li_element = self.driver.find_element(By.XPATH, '//a[@href="/about/"]')
        time.sleep(1)
        li_element.click()

        time.sleep(1)
        li_element = self.driver.find_element(By.XPATH, '//a[@href="/contact/"]')
        time.sleep(1)
        li_element.click()

    def test_footer(self):
        self.driver.get('http://127.0.0.1:8000/')
        # Find all the link elements with class name "menu__link"
        link_elements = self.driver.find_elements(By.CLASS_NAME, "menu__link")
        #Loop through the link elements and click on each one
        # for i in range(len(link_elements)):
        #     self.driver.execute_script("arguments[0].scrollIntoView();", link_elements[i])
        #     time.sleep(1)
        #     link_elements[i].click()
        #     time.sleep(1)
        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Home"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Services"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Portfolio"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="About"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Contact"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Privacy Policy"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(1)
        li_element.click()
        time.sleep(1)
        self.driver.back()
        time.sleep(2)

        li_element = self.driver.find_element(By.XPATH, '//li/a[text()="Terms of Use"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", li_element)
        time.sleep(2)
        li_element.click()
        self.driver.back()
        time.sleep(2)