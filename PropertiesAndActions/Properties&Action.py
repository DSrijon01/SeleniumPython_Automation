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

## invoking Wait
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

## element Locator
element_input = wait.until(ec.presence_of_element_located((By.ID,"user_input")))

## Check if the element is displayed or not
element_input_displayed = element_input.is_displayed()

## Check if the element is enabled or not
element_input_enabled = element_input.is_enabled()
print("Element is Enabled", element_input_enabled)

## Check the element size
element_input_size = element_input.size
print("Size of element : ", element_input_size)

## Check the element location
element_input_location = element_input.location
print("Element location : ", element_input_location)

## Send Keys and Clear Keys
element_input.send_keys("Srijon")
time.sleep(2)
element_input.clear()

## Get Text from edit box
element_input.send_keys("Srijon Value")
time.sleep(5)

## P.N. - get_attribute() is case sensitive need to use small cap "value"
element_input_value = element_input.get_attribute("value")
print("Text sent to the edit box :", element_input_value)

## Check Is Selected
element_radiobutton = driver.find_element(By.XPATH, "//input[@type='radio' and @value='Button2']")
element_radiobutton.click()
print("Is Selected or Not : ",element_radiobutton.is_selected())

time.sleep(5)
driver.quit()




