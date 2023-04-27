
import time
from django.test import TestCase
from selenium import webdriver
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TOMMYS SEC
class ButtonTest(TestCase):
    def setUp(self):
        self.selenium = WebDriver()
        self.selenium.implicitly_wait(10)

    def tearDown(self):
        self.selenium.quit()

    def test_button(self):
        self.selenium.get(self.live_server_url)
        button = self.selenium.find_element_by_class_name('contact_us_button')
        button.click()
        wait = WebDriverWait(self.selenium, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, 'contact-form')))
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/contact/')

def test_rotating_word_animation(TestCase):
    # create a webdriver instance
    driver = webdriver.Chrome()

    # navigate to the page with the rotating word animation
    driver.get("http://localhost:8000")

    # wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "rotating-word")))

    # get the rotating word element
    rotating_word = driver.find_element(By.ID, "rotating-word")

    # get the initial word
    initial_word = rotating_word.text

    # wait for the animation to complete (3.5 seconds)
    time.sleep(3.5)

    # get the updated word
    updated_word = rotating_word.text

    # assert that the updated word is not the same as the initial word
    assert initial_word != updated_word

    # quit the webdriver instance
    driver.quit()
class TestWebsiteTextSlideOne(TestCase):

    def test_slide_one(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        example_element = driver.find_element_by_class_name("carousel-caption")
        p_element = example_element.find_element_by_tag_name("p")
        assert p_element.text == "MORASCO REMODELING"
        h5_element = example_element.find_element_by_tag_name("h5")
        assert h5_element.text == "Quality | Experience | Affordable | Personalized"
        h4_element = example_element.find_element_by_tag_name("h4")
        assert h4_element.text == " With over 10 years of experience, we have the skills to help with almost all your remodeling and repairing needs."
        a_element = example_element.find_element_by_tag_name("a")
        assert a_element.text == "Lets Get Started!"
        driver.quit()
    def test_slide_two(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        example_element = driver.find_element_by_class_name("carousel-item")
        p_element = example_element.find_element_by_tag_name("p")
        assert p_element.text == "MORASCO REMODELING"
        h1_element = example_element.find_element_by_tag_name("h5")
        assert h1_element.text == "X?X?X"
        a_element = example_element.find_element_by_tag_name("a")
        assert a_element.text == "Lets Get Started!"
        driver.quit()
    def test_slide_three(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        example_element = driver.find_element_by_xpath("//div[@id='carouselExampleIndicators']//div[@class='carousel-item'][2]")
        p_element = example_element.find_element_by_tag_name("p")
        assert p_element.text == "MORASCO REMODELING"
        h1_element = example_element.find_element_by_tag_name("h5")
        assert h1_element.text == "X?X?X"
        a_element = example_element.find_element_by_tag_name("a")
        assert a_element.text == "Lets Get Started!"
        driver.quit()
class HomePageButtonOne(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8000")

    def tearDown(self):
        self.driver.quit()

    def test_see_all_services_button(self):
        button = self.driver.find_element_by_xpath("//a[contains(text(),'See all the ways we can help')]")
        button.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, "Services")
class HomePageButtonTwo(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_learn_more_button(self):
        self.driver.get(self.live_server_url)
        learn_more_button = self.driver.find_element_by_class_name("contact_us_button")
        learn_more_button.click()
        self.assertEqual(self.driver.current_url, self.live_server_url + "/contact/")
class TestRotatingWord(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000")
        self.wait = WebDriverWait(self.driver, 10)

    def test_rotating_word(self):
        rotating_word = self.wait.until(EC.visibility_of_element_located((By.ID, "rotating-word")))
        initial_word = rotating_word.text
        self.assertIsNotNone(initial_word)

        words = ["BUILT", "DESIGNED", "DEVELOPED", "CREATED", "ENGINEERED", "MADE", "CONSTRUCTED", "CONCOCTED", "CONSTRUCTED"]
        index = 0
        for i in range(len(words)):
            self.assertEqual(rotating_word.text, words[index])
            index = (index + 1) % len(words)
            self.driver.implicitly_wait(4) # Wait for 3.5 seconds plus some extra time
         
    def tearDown(self):
        self.driver.quit()

# TOMMYS SEC



# ROMANS SEC
class index_page_tests(TestCase):
    
    def test_images_loading(self):
        response = self.client.get('/')
        self.assertContains(response, 'core/images/Squared/about-us-pic(1).jpg')

    def test_about_us_section(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="slanted-text-container"')

    def test_about_us_class(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="daddy-perry"')

    def test_services_banner_css_classes(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="banner-container"')
        self.assertContains(response, 'class="banner-item"')
        self.assertContains(response, 'class="banner-text"')
        self.assertContains(response, 'class="text-center"')

    def test_services_banner_images(self):
        response = self.client.get('/')
        self.assertContains(response, 'core/images/Squared/PXL_20210908_193124241(1).jpg')
        self.assertContains(response, 'core/images/Squared/IMG_20180509_162146(1).jpg')
        self.assertContains(response, 'core/images/after/bradley-basement-after.jpg')
        self.assertContains(response, 'core/images/normal_sized/heated_floor.jpg')

    def test_inline_css_services_banner(self):
        response = self.client.get('/')
        self.assertContains(response, 'style="display: flex; justify-content: center; align-items: center;"')
        self.assertContains(response, 'style="font-size: 2rem !important;"')
        self.assertContains(response, 'class="flex justify-center items-center h-full mt-5"')
# ROMANS SEC
