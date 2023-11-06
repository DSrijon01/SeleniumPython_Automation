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

## Locating Element By ID
driver.find_element(By.ID,"user_input").send_keys("Srijon")

## Locating Element by Class Name
driver.find_element(By.CLASS_NAME,"entertext").click()

## Locating Element by Name Only
driver.find_element(By.NAME,"textbox").send_keys("Srijon")

## Locating Element By Tag Name
driver.find_element(By.NAME,"input").send_keys("Srijon")

## Locating Element By using Link Text
driver.find_element(By.LINK_TEXT,"FORM").click()

## Locating Element By using Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT,"FOR").click()

# Make sure to close the driver when done
time.sleep(5)
driver.quit()



