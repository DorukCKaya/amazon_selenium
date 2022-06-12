from pages.base_page import BasePage
from utils.locator import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self,driver):
        self.locator = SearchPageLocators
        super().__init__(driver)

    def keyword_control(self):
        assert "SAMSUNG" in self.find_element(*self.locator.KEYWORD_ASSERTER).text

    def navigate_to_second_page(self):
        self.click(*self.locator.SECOND_PAGE)
        assert "page=2" in self.get_url()

    def navigate_to_third_product(self):
       self.find_elements(*self.locator.THIRD_PRODUCT)[2].click()