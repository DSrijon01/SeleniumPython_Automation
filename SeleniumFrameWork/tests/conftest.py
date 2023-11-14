import pytest
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.utilities.DriverClass import WebDriverClass
import time


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    driver.maximize_window()
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
    time.sleep(2)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
