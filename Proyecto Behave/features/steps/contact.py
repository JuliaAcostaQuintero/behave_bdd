from behave import *
from features.steps.helpers.locators import ContactFormLocators
from steps.pages.contact_form import ContactForm
from steps.pages.page_index import PageIndex
from selenium import webdriver


@given('the user is on the Contact page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    index_page = PageIndex(context.driver)
    context.driver.get('http://automationpractice.com/index.php')
    context.driver.implicitly_wait(5)
    index_page.click_contact_link()


@when('the user fills in the contact form')
def step_impl(context):
    contact_form = ContactForm(context.driver)
    contact_form.select_subject("Customer service")
    contact_form.enter_email("zaith.jexiel@icelogs.com")
    contact_form.enter_message("Message to send")


@when('the user clicks on the Send button')
def step_impl(context):
    contact_form = ContactForm(context.driver)
    contact_form.click_send()


@then('the contact message is sent')
def step_impl(context):
    if "Your message has been successfully sent to our team" in context.driver.find_element(*ContactFormLocators.confirm_message).text:
        assert True
