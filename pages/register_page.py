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
    MESSAGE_ERROR = (By.CLASS_NAME, 'error-message')

    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)
        self.driver.maximize_window()
        sleep(2)

    """Register1"""
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

    """@Register2"""
    def set_empty_email(self, text):
        self.type(self.INPUT_EMAIL, text)
        sleep(2)
    # second step is the same as in the previous scenario - click_register_button
    def error_message_is_displayed(self):
        assert self.is_element_displayed(self.MESSAGE_ERROR)
    def get_error_message_text(self):
        return self.get_text(self.MESSAGE_ERROR)

    """@Register3"""
    # first step is the same as in the previous scenario - set_random_email
    def set_empty_password(self, text):
        self.type(self.INPUT_PASSWORD, text)
        sleep(2)
    # next steps are the same as in the previous scenario - click_register_button
