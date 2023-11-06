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

## 7 Ways to Access the CSS selectors

# 1. Using ID name in CSS Selector (To write id name in css selector you need to add "#" before id value)
driver.find_element(By.CSS_SELECTOR,"#user_input").send_keys("Srijon")

# 2. Using Class Name in CSS Selector (To write class name in css selector you need to add "." before class name)
driver.find_element(By.CSS_SELECTOR,".entertext").send_keys("Srijon")

# 3. Using " Tag name("input") and name " Attribute value as css_selector
driver.find_element(By.CSS_SELECTOR,"input[name=textbox]").send_keys("Srijon")

# 4. Using " Tag name("input"),className and name " Attribute value as css_selector
driver.find_element(By.CSS_SELECTOR,"input.entertext[name=textbox]").send_keys("Srijon")

# 5. “^” - Find elements using starts with a string value
driver.find_element(By.CSS_SELECTOR,"input[class^='en']").send_keys("Srijon")

# 6. “$” - Find elements using Ends with a string value
driver.find_element(By.CSS_SELECTOR,"input[class$='xt']").send_keys("Srijon")

# 7. “*” - Find elements using contains a substring.
driver.find_element(By.CSS_SELECTOR,"input[class*='ter']").send_keys("Srijon")

time.sleep(2)
driver.quit()