from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# Rest of your code

# Make sure to close the driver when done
driver.quit()
