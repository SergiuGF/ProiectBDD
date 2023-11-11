from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class CarPage(BasePage):
    PRODUCT_PAGE = "https://www.compari.ro/cafetiere-filtre-de-cafea-c3174/philips/ep2236-40-p590842329/"
    EXPAND_BUTTON = By.XPATH, '//*[@id="micro-data"]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/a[2]'
    NEGRU_OPTION = By.XPATH, '//*[@id="micro-data"]/div[3]/div[2]/div[2]/table/tbody/tr/td[3]'
    CUMPARA_BUTTON = By.XPATH, '//*[@id="micro-data"]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]'
    SPRE_COS_BUTTON = By.CLASS_NAME, 'c-cart-confirm__button--cart'
    PRODUCT = By.CLASS_NAME, 'c-card__product'
    def navigate_to_product_page(self):
        self.go_to(self.PRODUCT_PAGE)
        self.driver.maximize_window()
        sleep(2)
    def click_expand_button(self):
        self.click(self.EXPAND_BUTTON)
        sleep(2)
    def click_negru_option(self):
        self.click(self.NEGRU_OPTION)
        sleep(2)
    def click_cumpara_button(self):
        self.click(self.CUMPARA_BUTTON)
        sleep(2)
    def click_spre_cos_button(self):
        self.click(self.SPRE_COS_BUTTON)
        sleep(2)
    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)
        sleep(2)