from behave import *


@given('I am on the Home Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()

"""@Search1"""
@when('I click on the Search Bar')
def step_impl(context):
    context.home_page.click_search_bar()
@when('I insert ”tableta Samsung Galaxy” in the Search Bar')
def step_impl(context):
    context.home_page.search_for_products("tableta Samsung Galaxy")
@when('I click Search button')
def step_impl(context):
    context.home_page.click_search_button()
@then('At least 10 products are displayed')
def step_impl(context):
    assert context.home_page.check_product_quantity() >= 10

"""@Filter"""
@when('I click on the "Telefoane mobile" - under "Electronice" tab')
def step_impl(context):
    context.home_page.click_mobile()
@when('I click "Valori individuale" - under "Pret" tab')
def step_impl(context):
    context.home_page.click_value()
@when('I set the min value at 1000')
def step_impl(context):
    context.home_page.set_min_value("1000")
@when('I set the max value at 2000')
def step_impl(context):
    context.home_page.set_max_value('2000')
@when('I click "ok" button - under "Pret" tab')
def step_impl(context):
    context.home_page.click_ok_button()
@then('All products displayed are between 1000 and 2000 lei')
def step_impl(context):
    for price in context.home_page.check_product_prices():
        assert price >= 1000 and price <= 2000

"""@Test_URL"""
@when('I click on the Cart button')
def step_impl(context):
    context.home_page.click_cart_page()
@then('I am redirected to the Cart Page "https://checkout.compari.ro/"')
def step_impl(context):
    assert context.home_page.test_url() == "https://checkout.compari.ro/"

"""@Comparatie"""
@when('I click on the "Aparat foto" button')
def step_impl(context):
    context.home_page.click_aparat_foto_page()
@when('I check "Comparare" checkbox in the first product tab')
def step_impl(context):
    context.home_page.check_comparare()
@when('I click on the "Comparatie" button')
def step_impl(context):
    context.home_page.click_comparatie()
@then('The selected product is displayed')
def step_impl(context):
    context.home_page.is_selected_product_displayed()

