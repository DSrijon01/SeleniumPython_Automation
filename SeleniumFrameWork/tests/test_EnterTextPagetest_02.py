import unittest
import pytest
import time
from SeleniumFrameWork.pages.EnterTextPage import EnterText
import SeleniumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        cl.allureLogs("App Opened")
        self.et.clickOnLocatorsPage()
    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        time.sleep(2)
        cl.allureLogs("Next Test Executed")
        self.et.enterText()
        self.et.clickOnSubmitButton()
        self.et.takeScreenshot("Test Successfull Screen Shot for EnterText Page")

