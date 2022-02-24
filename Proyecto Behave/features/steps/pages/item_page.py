from helpers.locators import ItemPageLocators
from helpers.locators import CheckoutLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

    def select_size(self, text):
        dropdown = Select(self.driver.find_element(
            *ItemPageLocators.size_dropdown))
        dropdown.select_by_visible_text(text)

    def select_quantity(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*ItemPageLocators.plus_button).click()

    def add_to_cart(self):
        self.driver.find_element(*ItemPageLocators.add_cart_button).click()
#        WebDriverWait(self.driver, 10).until(
#            EC.presence_of_element_located(*ItemPageLocators.proceed_checkout))
        self.driver.find_element(*ItemPageLocators.proceed_checkout).click()
        self.driver.find_element(*CheckoutLocators.proceed_checkout_2).click()

    def quick_view(self):

        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(
            *ItemPageLocators.product_container))
        actions.perform()
#        WebDriverWait(self.driver, 5).until(
#            EC.presence_of_element_located(*ItemPageLocators.quick_view))
#        self.driver.find_element(*ItemPageLocators.quick_view).click()
