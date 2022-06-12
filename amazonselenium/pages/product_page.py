from pages.base_page import BasePage
from utils.locator import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    product = ""
    PRODUCT_TITLE = (By.ID, "productTitle")
    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    ITEM_ADDED_TO_CART_TITLE = (By.CLASS_NAME, "huc-atwl-header-small")
    VIEW_YOUR_LIST_BTN = (By.ID, "huc-view-your-list-button")

    def __init__(self, driver):
        self.locator = ProductPageLocators
        super().__init__(driver)

    def add_to_list(self):
        self.product = self.driver.find_element(*self.locator.PRODUCT_TITLE).text
        self.click(*self.locator.ADD_TO_LIST_BTN)

    def navigate_to_list(self):
        self.click(*self.locator.VIEW_YOUR_LIST_BTN)