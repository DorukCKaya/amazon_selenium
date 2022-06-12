from pages.base_page import BasePage
from pages.product_page import ProductPage
from utils.locator import ListPageLocators, ProductPageLocators
from selenium.webdriver.common.by import By


class ListPage(BasePage):

    DELETE_BTN = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.CSS_SELECTOR, ".a-alert-inline-success .a-alert-content")

    def __init__(self, driver):
        self.product_page = ProductPage(driver)
        self.locator = ListPageLocators
        self.product_page_locator = ProductPageLocators
        super().__init__(driver)

    def remove_product_from_list(self):
        self.click(*self.locator.DELETE_BTN)