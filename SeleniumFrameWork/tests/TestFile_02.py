import time

from SeleniumFrameWork.utilities.DriverClass import WebDriverClass
from SeleniumFrameWork.base.BasePage import BaseClass

web_driver = WebDriverClass()

driver = web_driver.getWebDriver("chrome")
base_page = BaseClass(driver)

## Launch Webpage with Base Page
base_page.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")

## Get web Element Using Base Page Locator type
base_page.sendText("Srijon", "user_input", "id")
time.sleep(5)

## Using locator Type Xpath
base_page.clickOnElement("/html/body/div[1]/div/div[3]/section/div[2]/div/form/input[3]","xpath")
time.sleep(5)

## Using the Scroll to Function
base_page.scrollTo("submitbutton", "id")
base_page.clickOnElement("submitbutton", "id")

## Using is displayed function
display_element = base_page.isElementDisplayed("Form", "link")
print(display_element)
base_page.clickOnElement("Form", "link")
