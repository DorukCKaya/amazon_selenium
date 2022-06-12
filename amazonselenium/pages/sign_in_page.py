from pages.base_page import BasePage
from utils.locator import SignInPageLocators


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = SignInPageLocators
        super().__init__(driver)

    def sign_in(self):
        self.fill(self.locator.EMAIL_ADRESS, *self.locator.EMAIL_BOX)
        self.click(*self.locator.CONTINUE_BUTTON)
        self.fill(self.locator.PASSWORD, *self.locator.PASSWORD_BOX)
        self.click(*self.locator.SIGN_IN_BUTTON)
