from pages.base_page import BasePage
from utils.locator import SignInPageLocators


class SignInPage(BasePage):

    EMAIL_ADRESS = "yourmail"
    EMAIL_BOX = (By.ID, "ap_email")
    CONTINUE_BTN = (By.ID, "continue")
    PASSWORD = "yourpw"
    PASSWORD_BOX = (By.ID, "ap_password")
    SIGN_IN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        self.locator = SignInPageLocators
        super().__init__(driver)

    def sign_in(self):
        self.fill(self.locator.EMAIL_ADRESS, *self.locator.EMAIL_BOX)
        self.click(*self.locator.CONTINUE_BTN)
        self.fill(self.locator.PASSWORD, *self.locator.PASSWORD_BOX)
        self.click(*self.locator.SIGN_IN_BTN)
