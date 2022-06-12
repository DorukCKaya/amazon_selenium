from pages.base_page import BasePage
from utils.locator import ProductPageLocators


class ProductPage(BasePage):

    product = ""

    def __init__(self, driver):
        self.locator = ProductPageLocators
        super().__init__(driver)

    def add_to_list(self):
        self.product = self.driver.find_element(*self.locator.PRODUCT_TITLE).text
        self.click(*self.locator.ADD_TO_LIST_BUTTON)

    def is_product_added_to_list(self):
        assert self.product == self.find_element(*self.locator.ITEM_ADDED_TO_CART_TITLE).text

    def navigate_to_list(self):
        self.click(*self.locator.VIEW_YOUR_LIST_BUTTON)