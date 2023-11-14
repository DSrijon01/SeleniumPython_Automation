import time
from SeleniumFrameWork.utilities.DriverClass import WebDriverClass
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.ContactFormPage import ContactForm

## Initiate the web Drivers from DriverClass
wd = WebDriverClass()
driver = wd.getWebDriver("chrome")
driver.maximize_window()

## Import Base Class from Base Page
bp = BaseClass(driver)

## Contact Form Page from Pages
cf = ContactForm(driver)

## Open the Site US form page
bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")

## Go the Form Page
cf.clickContactForm()

cf.verifyFormPage()

cf.enterName()

cf.enterEmail()

cf.selectGender()

cf.enterMessage()

cf.getCaptcha()

cf.enterCaptcha()

cf.screenShot("Form Submission Completed")

cf.clickOnPostButton()


time.sleep(5)