from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import re


class HomePage(BasePage):
    HOME_PAGE_URL = "https://www.compari.ro/"
    SEARCH_BAR = By.CLASS_NAME, "c-search__input"
    SEARCH_BUTTON = By.CLASS_NAME, "c-search__button"
    PRODUCTS = By.CLASS_NAME, "product-box"
    MOBILE_TAB = By.LINK_TEXT, "Telefoane mobile"
    PRICE_VALUE = By.XPATH, '//*[@id="morefilter-pret"]/a/span[1]'
    MIN_VALUE = By.NAME, "pret_minValue"
    MAX_VALUE = By.NAME, "pret_maxValue"
    OK_BUTTON = By.XPATH, '//*[@id="cf_pret"]/span[2]/a'
    PRODUCT_PRICES = By.CLASS_NAME, "price"
    CART_PAGE = By.CSS_SELECTOR, '#header-cart-icon > svg'


    def navigate_to_home_page(self):
        self.go_to(self.HOME_PAGE_URL)
        self.driver.maximize_window()
        sleep(2)
    def click_search_bar(self):
        self.click(self.SEARCH_BAR)
        sleep(2)
    def search_for_products(self, text):
        self.type(self.SEARCH_BAR, text)
        sleep(2)
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        sleep(2)
    def check_product_quantity(self):
        found_products = self.find_multiple(self.PRODUCTS)
        return len(found_products)

    def click_mobile(self):
        self.click(self.MOBILE_TAB)
        sleep(2)
    def click_value(self):
        self.click(self.PRICE_VALUE)
        sleep(2)
    def set_min_value(self, text):
        self.type(self.MIN_VALUE, text)
        sleep(2)
    def set_max_value(self, text):
        self.type(self.MAX_VALUE, text)
        sleep(2)
    def click_ok_button(self):
        self.click(self.OK_BUTTON)
        sleep(2)
    def check_product_prices(self):
        product_prices_text = [price.text for price in self.find_multiple(self.PRODUCT_PRICES)]
        prices_list = [re.sub(r'[^\d,]', '', item) for item in product_prices_text if item.strip()]
        prices_list_int = [int(item.split(',')[0]) for item in prices_list]
        return prices_list_int

    def click_cart_page(self):
        self.click(self.CART_PAGE)
        sleep(2)

    def test_url(self,):
        current_url = self.current_url()
        return current_url