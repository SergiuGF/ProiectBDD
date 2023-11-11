from behave import *


@given('I am on the "Philips EP2236/40" Page')
def step_impl(context):
    context.cart_page.navigate_to_product_page()
@when('I click on the expand button')
def step_impl(context):
    context.cart_page.click_expand_button()
@when('I click on the "Negru" option')
def step_impl(context):
    context.cart_page.click_negru_option()
@when('I click on the "Cumpara" button')
def step_impl(context):
    context.cart_page.click_cumpara_button()
@when('I click on the "Spre cos" button')
def step_impl(context):
    context.cart_page.click_spre_cos_button()
@then('the "Philips EP2236/40" product is displayed')
def step_impl(context):
    context.cart_page.is_product_displayed()