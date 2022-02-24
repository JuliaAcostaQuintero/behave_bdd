import unittest
from selenium.webdriver.common.by import By
from helpers.locators import PageDressesLocators
from helpers.locators import PageIndexLocators
from selenium.webdriver.support.ui import Select


class DressesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_dresses_link(self):
        self.driver.find_element(*PageIndexLocators.dresses_link).click()

    def select_options(self):
        self.driver.find_element(*PageDressesLocators.colors).click()
        self.driver.find_element(*PageDressesLocators.girly).click()
        select = Select(self.driver.find_element(
            *PageDressesLocators.products_sort))
        select.select_by_visible_text('Product Name: A to Z')
