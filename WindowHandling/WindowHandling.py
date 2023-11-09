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
assert "Selenium Template" in driver.title
time.sleep(2)

# Invoke wait
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

# Fetch the Current Window Name
window_name = driver.current_window_handle
print("Before switching ",window_name)
time.sleep(2)

# Navigate to the window
element = driver.find_element(By.CSS_SELECTOR, "div.breadcrumb-item:nth-child(5) > a:nth-child(1)")
element.click()
time.sleep(2)

# Navigate to the window Element
window_element = driver.find_elements(By.TAG_NAME,"input")

## Click on the Pop-up Window 2
for popup_w in window_element:
    popup_value = popup_w.get_attribute("value")
    if popup_w == "Open a Popup Window2":
        popup_w.click()


time.sleep(10)
#
# # Print the list of windows are present on the screen in present session
# windows = driver.window_handles
# for window in windows:
#     print("Window List: ", window)
#
# # Wait for the new window to open
# wait.until(ec.new_window_is_opened(windows))
#
# # Switch to Required window
# driver.switch_to.window(windows[1])