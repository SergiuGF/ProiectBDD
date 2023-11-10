from behave import *


@given("I am on the Register Page")
def step_impl(context):
    context.register_page.navigate_to_register_page()
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
