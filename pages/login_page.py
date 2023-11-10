from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://www.compari.ro/login/"
    EMAIL_INPUT = (By.NAME, "uname")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        self.driver.maximize_window()
        sleep(2)
    def set_unregistred_email(self, text):
        self.type(self.EMAIL_INPUT, text)
        sleep(2)
    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)
        sleep(2)
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        sleep(2)
    def is_error_message_displayed(self):
        assert self.is_element_displayed(self.ERROR_MESSAGE)
        sleep(2)
    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)
