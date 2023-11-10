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
from selenium.webdriver.common.alert import Alert


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
driver.maximize_window()
element = driver.find_element(By.CSS_SELECTOR, "div.breadcrumb-item:nth-child(5) > a:nth-child(1)")
element.click()

time.sleep(2)

# Navigate to the window Element
window_element = driver.find_elements(By.TAG_NAME,"input")

## Click on the Pop-up Window 2
for popup_w in window_element:
    popup_value = popup_w.get_attribute("value")
    if popup_value == "Open a Popup Window2":
        popup_w.click()


time.sleep(10)

# Print the list of windows are present on the screen in present session
windows = driver.window_handles
for window in windows:
    print("Window List: ", window)


# Switch to Required window
driver.switch_to.window(windows[1])
driver.maximize_window()
time.sleep(2)

# New window
new_window_element = driver.find_element(By.ID,"f2")
driver.switch_to.frame(new_window_element)

# Switching to New window and performing action on Frame
new_window_element_2 = driver.find_element(By.NAME,"promtalert")
new_window_element_2.click()

## handle the Alert Window:
alert_button = Alert(driver)

text_p = alert_button.text
print(text_p)

alert_button.send_keys("Srijon")
alert_button.dismiss()

# Fetch the frame name from new window
data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)

# Driver Close
time.sleep(2)
driver.close()

# Driver Quit
time.sleep(5)
driver.quit()