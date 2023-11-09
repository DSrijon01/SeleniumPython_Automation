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

# Locate element
multi_select_element = driver.find_element(By.ID, "multiselect")

# Select MultiSelect
multi_select_options = Select(multi_select_element)

# Check if the element is a multislect or not
print("Check whether It Is a Multi Select or not : ", multi_select_options.is_multiple)

# List Down the values of Multi Select:
multi_select_values = multi_select_options.options

# Iterate through the multi Select Values
for multi_select_vl in multi_select_values:
    print(multi_select_vl.text)

# Select by Index
multi_select_options.select_by_index(1)

# Select by Value
multi_select_options.select_by_value("mOptionTWo")

# Select by Text
multi_select_options.select_by_visible_text("mOption3")

# Invoke DeSelect to DeSelect All
multi_select_options.deselect_all()

time.sleep(2)
driver.quit()

