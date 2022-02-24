from behave import *
from selenium import webdriver
from pages.page_index import *
from pages.item_page import *
from pages.checkout import *
from steps.helpers.locators import *
from selenium.webdriver.chrome.options import Options
import unittest


@given('the user is on the main page')
def step_impl(context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.driver.get("http://automationpractice.com/index.php")
    context.driver.implicitly_wait(5)


@when('the user searches for {item}')
def step_impl(context, item):
    #context.driver = webdriver.Chrome('chromedriver.exe')
    index = PageIndex(context.driver)
    index.search(item)


@then('the user sees {item} displayed on the results')
def step_impl(context, item):
    if context.driver.find_element(*ItemPageLocators.product_name) == item:
        assert True
