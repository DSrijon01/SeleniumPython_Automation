from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
import SeleniumFrameWork.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            # Initialize Chrome WebDriver using ChromeDriverManager
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            # Safari WebDriver initialization (no need for WebDriverManager for Safari)
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            # Initialize Firefox WebDriver using GeckoDriverManager
            driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
            self.log.info("FireFox Driver is initializing")

        return driver
