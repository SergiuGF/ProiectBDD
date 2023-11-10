from driver import Driver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()


def after_all(context):
    context.browser.close()
