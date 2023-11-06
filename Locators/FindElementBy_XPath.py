"""
1. Absolute XPath:
It uses from complete html root path to the required WebElement.
EX : "/html/body/div/div[2]/div[2]/div/div/div/div[2]/form/input[1]" (or)  "//form//input[1]"


'/'  - finding the element inside the parent element
'//' - finding the child or nested-child element inside the parent element

2. Relative Xpath :
It uses the direct path of a WebElement using (id,className,attribute values , sub-string,etc) to perform action on it.

i) EX : //tag[@attribute='value']
   "//*[@id='user_input']" or "//input[@id='user_input']"

ii) Using Contains ( Need to give partial value) :
    Syntax : "//tag[contains(@attribute,'partial value of attribute')]"
    Ex :     "//input[contains(@id,'user')]"  , "//a[contains(text(),'Form')]"

iii) Starts-With ( Need to give partial value) :
    Syntax: "//tag[starts-with(@attribute,'partial value of attribute')]"
    Ex :    "//input[starts-with(@id,'user')]"



"""



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
time.sleep(2)


## Finding Elements Through Xpath
element = driver.find_element(By.XPATH,"//a[contains(text(),'Form')]")
element.click()

