import time
from datetime import datetime
from traceback import print_stack
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import SeleniumFrameWork.utilities.CustomLogger as cl
import allure


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web Page Launched with URL: {} {}".format(url, title))
        except:
            self.log.info("Web Page Not Launched with URL: {} {}".format(url, title))
            print_stack()

    ## Fetch All Available Locator Type
    def getLocatorType(self, locatorType):
        ## Transforming Input into lowercase letters
        locatorType = locatorType.lower()

        ## For Locator Type id
        if locatorType == "id":
            return By.ID
        ## Locator Type Name
        elif locatorType == "name":
            return By.NAME
        ## Locator Type Class
        elif locatorType == "class":
            return By.CLASS_NAME
        ## Locator Type XPath
        elif locatorType == "xpath":
            return By.XPATH
        ## Locator type CSS
        elif locatorType == "css":
            return By.CSS_SELECTOR
        ## Locator Type Tag
        elif locatorType == "tag":
            return By.TAG_NAME
        ## Locator Type Link Text
        elif locatorType == "link":
            return By.LINK_TEXT
        ## Locator Type Partial Link
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locatorType + " entered is not found")
        return False

    def getWebElement(self, locatorValue, locatorType):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorByType)
        except:
            self.log.error("WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
        return webElement

    ## Invoking Wait for Element Visiblity: (We can declare this Earlier during Class fucntion invoke)
    def waitForElement(self, locatorValue, locatorType):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
        return webElement

    ## Click Event
    def clickOnElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()

    ## Send keys Event
    def sendText(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info("Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to Sent the text " + text + " in WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

    ## Fetch Text
    def getText(self, locatorValue, locatorType="id"):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info("Got the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to get the text " + elementText + " from WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

        return elementText

    ## Locate if the Element is visible or not
    def isElementDisplayed(self, locatorValue, locatorType):
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info("WebElement is Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("WebElement is not Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()

        return elementDisplayed

    ## Scroll to Event

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info("Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

    ## Save Screenshots method
    # def screenShot(self, screenshotName):
    #     fileName = screenshotName + "_" + (datetime.now().strftime("%d_%m_%y_%H_%M_%S")) + ".png"
    #     screenshotDirectory = "../screenshots/"
    #     screenshotPath = screenshotDirectory + fileName
    #     try:
    #         self.driver.save_screenshot(screenshotPath)
    #         self.log.info("Screenshot saved to path: " + screenshotPath)
    #     except:
    #         self.log.info("Unable to save screenshot to the path: " + screenshotPath)

    def screenShot(self, screenshotName):
        current_time = datetime.now()
        print("Current time:", current_time)  # Add this line to print the current time

        fileName = screenshotName + "_" + (current_time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot saved to path: " + screenshotPath)
        except:
            self.log.info("Unable to save screenshot to the path: " + screenshotPath)

    ## Save Screen shots Using Allure Reporting
    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=AttachmentType.PNG)
