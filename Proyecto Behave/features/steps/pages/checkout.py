from time import sleep
from helpers.locators import CheckoutLocators
from selenium.webdriver.common.action_chains import ActionChains


class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def user_name(self, username):
        self.driver.find_element(
            *CheckoutLocators.user_name).send_keys(username)

    def password(self, password):
        self.driver.find_element(
            *CheckoutLocators.password).send_keys(password)
        self.driver.find_element(*CheckoutLocators.sign_in_button).click()
        self.driver.find_element(*CheckoutLocators.process_address).click()

    def terms_of_service(self):
        checkbox = self.driver.find_element(
            *CheckoutLocators.terms_service)
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox)
        actions.click()
        actions.perform()
        self.driver.find_element(*CheckoutLocators.process_carrier).click()

    def pay_by_wire(self):
        self.driver.find_element(*CheckoutLocators.bank_wire_button).click()
        self.driver.find_element(
            *CheckoutLocators.confirm_order_button).click()
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(
            *CheckoutLocators.confirm_message))
        actions.perform()


#    def order_confirmation(self):
