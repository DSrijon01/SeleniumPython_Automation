import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## Initializing Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

## URL
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

## Invoking Implicit Wait
driver.implicitly_wait(10)

## Finding Elements Through Xpath
element = driver.find_element(By.XPATH,"//a[contains(text(),'Form')]")
element.click()