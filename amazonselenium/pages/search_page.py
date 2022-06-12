from pages.base_page import BasePage
from utils.locator import SearchPageLocators
from selenium.webdriver.common.by import By


class SearchPage(BasePage):

    KEYWORD_ASSERTER = (By.CLASS_NAME, "a-color-state.a-text-bold")
    SECOND_PAGE = (By.CLASS_NAME, "s-pagination-button")
    THIRD_PRODUCT = (By.CLASS_NAME, "a-link-normal.s-no-outline")

    def __init__(self,driver):
        self.locator = SearchPageLocators
        super().__init__(driver)

    def keyword_control(self):
        assert "SAMSUNG" in self.find_element(*self.locator.KEYWORD_ASSERTER).text

    def navigate_to_second_page(self):
        self.click(*self.locator.SECOND_PAGE)

    def navigate_to_third_product(self):
       self.find_elements(*self.locator.THIRD_PRODUCT)[2].click()