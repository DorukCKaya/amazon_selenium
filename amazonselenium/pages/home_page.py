from pages.base_page import BasePage
from utils.locator import HomePageLocators
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    BASE_URL = "https://www.amazon.com/"
    SIGN_IN_PAGE_BTN = (By.ID, "nav-link-accountList")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_KEYWORD = "SAMSUNG"
    HOME_PAGE_ASSERTER = (By.CSS_SELECTOR, "role='main'")

    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def navigate_to_sign_in(self):
        self.click(*self.locator.SIGN_IN_PAGE_BTN)

    def search_keyword(self):
        self.fill(self.locator.SEARCH_KEYWORD, *self.locator.SEARCH_BOX)
        self.click(*self.locator.SEARCH_BTN)
