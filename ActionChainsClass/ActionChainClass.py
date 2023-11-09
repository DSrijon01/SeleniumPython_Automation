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

element = driver.find_element(By.XPATH,"//a[contains(text(),'Form')]")

# Import the ActionChains Class

# 1. Create the object for ActionChains class
actions = ActionChains(driver)


# 2. Double click Operation
actions.double_click(element).perform()



# 3. Right click Operation
#actions.context_click().perform()
#actions.context_click(ele).perform()


time.sleep(5)
driver.quit()

