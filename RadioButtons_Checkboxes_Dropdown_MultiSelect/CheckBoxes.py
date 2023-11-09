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

# 1. find the list of radio buttons using locator (many)
element_check_boxes = driver.find_elements(By.NAME,"checkbox")
time.sleep(2)

## Check if the checkboxes are already checked or not

for checkbox in element_check_boxes:
    checkbox_value = checkbox.get_attribute("value")
    print(checkbox_value)

    if checkbox_value == "c1":
        if checkbox.is_selected():
            print("Checkbox is already checked.")
        else:
            checkbox.click()
            print("Checkbox is now checked.")
        break

# # 2. Using for loop iterate the list object and click on required checkbox
# for checkbox in element_check_box:
#     checkbox_value = checkbox.get_attribute("value")
#     print(checkbox_value)
#     if checkbox_value == "c2":
#         checkbox.click()
#         print("Is Selected : ",checkbox.is_selected())
#         break


time.sleep(2)
driver.quit()

