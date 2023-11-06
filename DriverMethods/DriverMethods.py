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
assert "Selenium Template" in driver.title
time.sleep(2)

## Maximize the Window
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()

## Finding Elements Through Xpath
element = driver.find_element(By.XPATH,"//a[contains(text(),'Form')]")
element.click()