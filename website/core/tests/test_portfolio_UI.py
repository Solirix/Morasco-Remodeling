import time
from django.test import LiveServerTestCase # needed for testing the UI
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager # this line and the next can be changed to use other browsers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# class TestUI(LiveServerTestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

#     def tearDown(self):
#         self.driver.quit()

#     def test_ask_us_button(self):
#         self.driver.get('http://127.0.0.1:8000/portfolio/')
        
#     def test_buttons_on_page(self):
#         # Replace the URL with the website you want to test
#         url = "https://example.com"

#         # Replace the button_text with the text of the buttons you want to test
#         button_text = "Click Me"

#         # Replace the path_to_driver with the path to your webdriver
#         path_to_driver = "/path/to/chromedriver"

#         # Set up the webdriver
#         driver = webdriver.Chrome(path_to_driver)
#         driver.get(url)

#         # Find all the buttons on the page with the specified text
#         buttons = driver.find_elements_by_xpath(f"//button[contains(text(), '{button_text}')]")

#         # Test each button by clicking it and verifying that it works
#         for button in buttons:
#             # Click the button
#             button.click()

#          # Wait for the page to load
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#             # Verify that the button worked by checking for a specific element on the page
#             try:
#                 success_message = driver.find_element_by_xpath("//p[contains(text(), 'Success')]")
#                 print(f"Button '{button_text}' worked!")
#             except:
#                 print(f"Button '{button_text}' didn't work.")

#         # Close the webdriver
#         driver.quit()