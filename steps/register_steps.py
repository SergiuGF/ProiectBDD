from behave import *


@given("I am on the Register Page")
def step_impl(context):
    context.register_page.navigate_to_register_page()

"""@Register1"""
@when('I set a new email')
def step_impl(context):
    context.register_page.set_random_email()
@when('I set password as "{text}"')
def step_impl(context, text):
    context.register_page.set_password(text)
@when('I click register button')
def step_impl(context):
    context.register_page.click_register_button()
@then('Success message is displayed')
def step_impl(context):
    context.register_page.is_success_message_displayed()

"""@Register2"""
@when("I insert ' ' in the mail input")
def step_impl(context):
    context.register_page.set_empty_email(" ")
@when('I click register button - Scenario 2')
def step_impl(context):
    context.register_page.click_register_button()
@then('Email error message is displayed')
def step_impl(context):
    context.register_page.error_message_is_displayed()
@then('Email error text contains "Completarea campului este obligatorie!" message')
def step_impl(context):
    context.register_page.get_error_message_text()

"""@Register3"""
@when("I set a new email - Scenario 3")
def step_impl(context):
    context.register_page.set_random_email()
@when("I insert ' ' in the password input")
def step_impl(context):
    context.register_page.set_empty_password(' ')
@when("I click register button - Scenario 3")
def step_impl(context):
    context.register_page.click_register_button()
@then('Password error message is displayed')
def step_impl(context):
    context.register_page.error_message_is_displayed()
@then('Password error text contains "Completarea campului este obligatorie!" message')
def step_impl(context):
    context.register_page.get_error_message_text()
