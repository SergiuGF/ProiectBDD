from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
from time import sleep


class RegisterPage(BasePage):
    REGISTER_PAGE_URL = "https://www.compari.ro/inregistrare/"
    INPUT_EMAIL = (By.NAME, "uname")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_REGISTER = (By.ID, "reg-submit")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "desc")
    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)
        self.driver.maximize_window()
        sleep(2)
    def set_random_email(self):
        random_number = random.randint(1, 999)
        andress_email = f'test_compari{random_number}@itfactory.ro'
        self.type(self.INPUT_EMAIL, andress_email)
        sleep(5)
    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)
        sleep(2)
    def click_register_button(self):
        self.click(self.BUTTON_REGISTER)
        sleep(2)
    def is_success_message_displayed(self):
        assert self.is_element_displayed(self.MESSAGE_SUCCESS)

