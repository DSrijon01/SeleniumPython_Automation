import time
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

## Initializing Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
## URL
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

## Invoking Explicit Wait
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

## Invoking Wait for Element
element = wait.until(EC.presence_of_element_located((By.ID, "user_input")))
element.send_keys("Srijon")

time.sleep(5)
driver.quit()
