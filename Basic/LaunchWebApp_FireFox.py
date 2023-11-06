from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
# Initialize Firefox WebDriver using GeckoDriverManager
driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# Rest of your code

# Make sure to close the driver when done
driver.quit()
