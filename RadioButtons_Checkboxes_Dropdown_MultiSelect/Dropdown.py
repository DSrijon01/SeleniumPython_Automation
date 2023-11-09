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

# 2. Locate Element
dropdown_element = wait.until(ec.presence_of_element_located((By.ID,"dropdown")))
dropdown_element.click()

# 3. Objects for Select Class
drop_down_options = Select(dropdown_element)

# 4. List the values in dropdown and print them
drop_down_values = drop_down_options.options
for drop_down_vl in drop_down_values:
    print(drop_down_vl.text )

# 5. Select an Option by "Index"
drop_down_options.select_by_index(2)
time.sleep(2)

# 6. Select an Option by "Value"
drop_down_options.select_by_value("OptionThree")
time.sleep(2)

# 7. Select an option by "Text"
drop_down_options.select_by_visible_text("Option5")

time.sleep(5)
driver.quit()




