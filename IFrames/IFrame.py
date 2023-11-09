import time
from selenium import webdriver
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
## Import Select Class
from selenium.webdriver.support.select import Select


## Initializing Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

## URL
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

# 1. Invoke Wait
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

## Click on Frame to navigate to the next frame
frame = driver.find_element(By.CSS_SELECTOR,"div.breadcrumb-item:nth-child(4) > a:nth-child(1)")
frame.click()


# Locate elements (many)
iframe_element = driver.find_elements(By.TAG_NAME, "iframe")
# List of the iFrame Elements
print("list of iFrame :", len(iframe_element))

# Switch and Fetch Data to Iframe 1
time.sleep(2)
iframe = driver.find_element(By.ID,"f1")
driver.switch_to.frame(iframe)
iframe1_button = driver.find_element(By.NAME, "promtalert")
time.sleep(2)
data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)

# Switch to default Content
time.sleep(2)
driver.switch_to.default_content()

## Check if it has switched to the content context or not
data = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",data.text)
