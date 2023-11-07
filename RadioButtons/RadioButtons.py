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

# 1. find the list of radio buttons using locator
element_radio_button = driver.find_elements(By.NAME,"radio")
time.sleep(2)

# 2. Using for loop iterate the list object and click on required option
for radiobutton in element_radio_button:
    radiobutton_value = radiobutton.get_attribute("value")
    print(radiobutton_value)
    if radiobutton_value == "Button2":
        radiobutton.click()
        print("Is Selected : ",radiobutton.is_selected())
        break



time.sleep(2)
driver.quit()