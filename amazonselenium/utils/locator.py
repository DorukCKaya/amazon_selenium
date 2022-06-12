from selenium.webdriver.common.by import By


class HomePageLocators(object):
    BASE_URL = "https://www.amazon.com/"
    SIGN_IN_PAGE_BTN = (By.ID, "nav-link-accountList")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_KEYWORD = "SAMSUNG"
    HOME_PAGE_ASSERTER = (By.CSS_SELECTOR, "role='main'")


class SignInPageLocators(object):
    EMAIL_ADRESS = "yourmail"
    EMAIL_BOX = (By.ID, "ap_email")
    CONTINUE_BTN = (By.ID, "continue")
    PASSWORD = "yourpw"
    PASSWORD_BOX = (By.ID, "ap_password")
    SIGN_IN_BTN = (By.ID, "signInSubmit")


class SearchPageLocators(object):
    KEYWORD_ASSERTER = (By.CLASS_NAME, "a-color-state.a-text-bold")
    SECOND_PAGE = (By.CLASS_NAME, "s-pagination-button")
    THIRD_PRODUCT = (By.CLASS_NAME, "a-link-normal.s-no-outline")


class ProductPageLocators(object):
    product = ""
    PRODUCT_TITLE = (By.ID, "productTitle")
    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    ITEM_ADDED_TO_CART_TITLE = (By.CLASS_NAME, "huc-atwl-header-small")
    VIEW_YOUR_LIST_BTN = (By.ID, "huc-view-your-list-button")


class ListPageLocators(object):
    DELETE_BTN = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.CSS_SELECTOR, ".a-alert-inline-success .a-alert-content")
