import unittest
from helpers.locators import PageIndexLocators


class PageIndex:
    def __init__(self, driver):
        self.driver = driver

    def search(self, item):
        self.driver.find_element(
            *PageIndexLocators.query_top).send_keys(item)
        self.driver.find_element(*PageIndexLocators.query_button).click()

    def click_item(self):
        self.driver.find_element(*PageIndexLocators.item_link).click()

    def click_contact_link(self):
        self.driver.find_element(*PageIndexLocators.contact_link).click()


if __name__ == '__main__':
    unittest.main()
