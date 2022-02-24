from helpers.locators import ContactFormLocators
from selenium.webdriver.support.ui import Select


class ContactForm:
    def __init__(self, driver):
        self.driver = driver

    def select_subject(self, subject):
        select = Select(self.driver.find_element(
            *ContactFormLocators.subject_dropdown))
        select.select_by_visible_text(subject)

    def enter_email(self, email):
        self.driver.find_element(
            *ContactFormLocators.email_field).send_keys(email)

    def attach_file(self, file_path):
        self.driver.find_element(
            *ContactFormLocators.attach_field).send_keys(file_path)

    def enter_message(self, message):
        self.driver.find_element(
            *ContactFormLocators.message_body).send_keys(message)

    def click_send(self):
        self.driver.find_element(*ContactFormLocators.send_button).click()

    def confirm_sent(self):
        self.assertTrue('Your message has been successfully sent to our team.' in self.driver.find_element(
            *ContactFormLocators.confirm_message).text)
