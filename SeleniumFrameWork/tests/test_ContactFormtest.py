import unittest
import pytest
import time
from SeleniumFrameWork.pages.ContactFormPage import ContactForm
from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self,request):
        self.driver = request.getfixturevalue("beforeClass")
        self.bp = BaseClass(self.driver)
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=1)
    def test_formPage(self):
        time.sleep(5)
        self.cf.clickContactForm()
        self.cf.verifyFormPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.selectGender()
        self.cf.enterMessage()
        self.cf.enterCaptcha()
        self.cf.screenShot("Form Submission Completed With ConfTest")
        self.cf.clickOnPostButton()


