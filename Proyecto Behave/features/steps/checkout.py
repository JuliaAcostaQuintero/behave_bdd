from behave import *
from selenium import webdriver
from pages.page_index import *
from pages.item_page import *
from pages.checkout import *
from selenium.webdriver.chrome.options import Options


@when('the user searches for blouses')
def step_impl(context):
    index = PageIndex(context.driver)
    context.driver.implicitly_wait(5)
    index.search("blouses")
    index.click_item()


@when('the user follows the checkout steps')
def step_impl(context):
    items = ItemPage(context.driver)
    checkout = Checkout(context.driver)
    items.select_size('L')
    items.select_quantity(4)
    items.add_to_cart()
    checkout.user_name('zaith.jexiel@icelogs.com')
    checkout.password('12345')
    checkout.terms_of_service()
    checkout.pay_by_wire()


@then('the user succesfully purchases the blouses')
def step_impl(context):
    pass
