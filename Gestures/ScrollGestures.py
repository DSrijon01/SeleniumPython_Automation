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
## Page Title Assertion
assert "Selenium Template" in driver.title
time.sleep(2)

## Invoking Wait
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

## Element Navigation
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"div.breadcrumb-item:nth-child(2) > a:nth-child(1)"))).click()
wait.until(ec.presence_of_element_located((By.ID,"reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.ID,"name"))).send_keys("Srijon")
wait.until(ec.presence_of_element_located((By.ID,"email"))).send_keys("Srijon@gmail.com")
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"input.form-radio:nth-child(2)"))).click()
wait.until(ec.presence_of_element_located((By.ID,"message"))).send_keys("Srijon")
captcha = wait.until(ec.presence_of_element_located((By.ID,"captcha_image")))
wait.until(ec.presence_of_element_located((By.ID,"captcha"))).send_keys(captcha.text)

postButton = wait.until(ec.presence_of_element_located((By.ID,"btnContactUs")))

# Scroll Gesture
actions = ActionChains(driver)
actions.move_to_element(postButton).perform()
postButton.click()

time.sleep(5)
driver.quit()