from pages.base_page import BasePage
from pages.product_page import ProductPage
from utils.locator import ListPageLocators, ProductPageLocators


class ListPage(BasePage):

    def __init__(self, driver):
        self.product_page = ProductPage(driver)
        self.locator = ListPageLocators
        self.product_page_locator = ProductPageLocators
        super().__init__(driver)

    def remove_product_from_list(self):
        self.click(*self.locator.DELETE_BUTTON)

    def is_item_removed(self):
        assert "Deleted" == self.visibility_element(self.locator.DELETED_TEXT).text

