from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

"""@Login1"""
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

"""@Login2"""
@when('I insert " " in the mail input')
def step_impl(context):
    context.login_page.set_empty_email(" ")
@when('I click on the login button - Scenario 2')
def step_impl(context):
    context.login_page.click_login_button()
@then('Email error message is displayed - Scenario 2')
def step_impl(context):
    context.login_page.is_error_message_displayed()
@then('Email error text contains "{message}" message - Scenario 2')
def step_impl(context, message):
    assert message in context.login_page.get_error_message_text()

"""@Login3"""
@when('I insert an valid email in the mail input')
def step_impl(context):
    context.login_page.set_valid_email("testingemail2352@gmail.com")
@when('I insert an valid password in the password input')
def step_impl(context):
    context.login_page.set_valid_password("Passfortesting123!")
@when('I click on the login button - Scenario 3')
def step_impl(context):
    context.login_page.click_login_button()
@then('I am redirected to account page')
def step_impl(context):
    assert context.home_page.test_url() == "https://www.compari.ro/users/452083/#settings-account"
