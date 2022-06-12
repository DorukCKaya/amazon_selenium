import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.locator import HomePageLocators


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.locator = HomePageLocators
        option = Options()
        option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.locator.BASE_URL)

    def tearDown(self):
        self.driver.close()
