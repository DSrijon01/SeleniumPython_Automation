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

## Initializing Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

## URL
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

## Get the nexr URL
driver.get("http://www.dummypoint.com/Form.html")
time.sleep(2)

## Press Browser Back Button
driver.back()
time.sleep(2)

## Press Browser Forward Button
driver.forward()
time.sleep(2)

# Refresh Browser
driver.refresh()

time.sleep(5)
driver.quit()