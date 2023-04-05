#!/usr/bin/env python
from selenium.webdriver.common.by import By
from framework.base.base_page import BasePage, GenericLocators


class GooglePageLocators(object):

    LOGO = (By.XPATH, "//*[@id='logo']")
    SEARCH_FIELD = (By.XPATH, "/html/body/ntp-app//div/div[1]/ntp-realbox//div/input")


class GooglePage(BasePage):

    def __init__(self, driver):
        super(GooglePage, self).__init__(driver)
        self.driver = driver
        self.generic_locators = GenericLocators
        self.google_page_locators = GooglePageLocators

    def is_logo_visible_on_the_page(self):
        self.wait_for_element_to_appear(*self.login_page_locators.LOGO)
        logo = self.is_element_visible(*self.login_page_locators.LOGO)
        return logo

    def enter_keyword_into_search_field_and_press_enter(self, search_keyword):
        self.wait_for_element_to_appear(*self.login_page_locators.SEARCH_FIELD)
        self.find(*self.login_page_locators.SEARCH_FIELD).clear()
        self.find(*self.login_page_locators.SEARCH_FIELD).send_keys(search_keyword)
        self.press_enter(SEARCH_FIELD)
