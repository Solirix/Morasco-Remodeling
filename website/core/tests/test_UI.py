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

        # Find the image element
        WebElement imageElement = driver.findElement(By.xpath("//img[@src='core/images/mr_logo.png']"));

        # Get the width and height of the image
        int width = imageElement.getSize().getWidth();
        int height = imageElement.getSize().getHeight();

        # Verify that the width and height of the image are correct
        assertEquals(width, 300);
        assertEquals(height, 100);

        # Verify that all links on the page are working correctly
        List<WebElement> links = driver.findElements(By.tagName("a"));
        for (WebElement link : links) {
            String href = link.getAttribute("href");
            driver.get(href);
            assertEquals(driver.getCurrentUrl(), href);
        }

