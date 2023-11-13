from SeleniumFrameWork.base.BasePage import BaseClass
class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## Defining All the Locators in Contact Form Page:

    _contactFromPage = "Form"  # link
    _formPage = "reused_form"  # id
    _enterName = "name"  # id
    _enterEmail = "email"  # id
    _selectGender = "input.form-radio:nth-child(2)" # CSS
    _enterMessage = "message"  # id
    _getCaptcha = "captcha_image"  # id
    _enterCaptcha = "captcha"  # id
    _postButton = "btnContactUs"  # id

    ## Click on the form Link Page
    def clickContactForm(self):
        self.clickOnElement(self._contactFromPage, "link")

    ## Verify If the form page is open or not
    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, "id")
        assert element == True

    ## Enter Your name on the form
    def enterName(self):
        self.sendText("Srijon", self._enterName, "id")

    ## Enter your Email Address on the form
    def enterEmail(self):
        self.sendText("Srijon@gmail.com", self._enterEmail, "id")

    ## Select the radio Button for Gender
    def selectGender(self):
        self.clickOnElement(self._selectGender, "css")

    ## Enter your Message in the form
    def enterMessage(self):
        self.sendText("This is Srijon", self._enterMessage, "id")

    ## Get the Captcha Element
    def getCaptcha(self):
        cap = self.getText(self._getCaptcha, "id")
        return cap

    ## Enter the Captcha
    def enterCaptcha(self):
        self.sendText(self.getCaptcha(), self._enterCaptcha, "id")

    ## Scroll and Click on the Submit/Post Button
    def clickOnPostButton(self):
        self.scrollTo(self._postButton, "id")
        self.clickOnElement(self._postButton, "id")