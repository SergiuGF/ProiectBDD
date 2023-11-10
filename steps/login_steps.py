from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()
@when('I insert an unregistered email in the mail input')
def step_impl(context):
    (context.login_page.set_unregistred_email("email_neinregistrat@host.com"))
@when('I insert a password in the password input')
def step_impl(context):
    context.login_page.set_password("password")
@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()
@then('The error message is displayed')
def step_impl(context):
    context.login_page.is_error_message_displayed()
@then('The error message contains "{message}" message')
def step_impl(context, message):
    assert message in context.login_page.get_error_message_text()


