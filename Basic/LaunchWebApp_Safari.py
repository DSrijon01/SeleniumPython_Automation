from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()

## Will Only Work on Mac Webdriver Manager Doesn't support Safari
