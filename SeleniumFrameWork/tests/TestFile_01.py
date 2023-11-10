from SeleniumFrameWork.utilities.DriverClass import WebDriverClass
from SeleniumFrameWork.base.BasePage import BaseClass

web_driver = WebDriverClass()

driver = web_driver.getWebDriver("chrome")
base_page = BaseClass(driver)

## Lauch Webpage with Driver
# driver.get("http://www.dummypoint.com/seleniumtemplate.html")

## Launch Webpage with Base Page
base_page.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")

