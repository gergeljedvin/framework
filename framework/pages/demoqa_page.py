#!/usr/bin/env python
from selenium.webdriver.common.by import By
from framework.base.base_page import BasePage, GenericLocators


class DemoqaPageLocators(object):

    LOGO = (By.XPATH, "/html/body/div[2]/header/a/img")
    ELEMENTS_CARD = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")
    ELEMENTS_PAGE_HEADER = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div")


class DemoqaPage(BasePage):

    def __init__(self, driver):
        super(DemoqaPage, self).__init__(driver)
        self.driver = driver
        self.generic_locators = GenericLocators
        self.demoqa_page_locators = DemoqaPageLocators

    def is_logo_visible_on_the_page(self):
        self.wait_for_element_to_appear(*self.demoqa_page_locators.LOGO)
        logo = self.is_element_visible(*self.demoqa_page_locators.LOGO)
        return logo

    def is_elements_card_visible_on_the_page(self):
        self.wait_for_element_to_appear(*self.demoqa_page_locators.ELEMENTS_CARD)
        elements_card = self.is_element_visible(*self.demoqa_page_locators.ELEMENTS_CARD)
        return elements_card

    def click_on_the_elements_card(self):
        self.wait_for_element_to_appear(*self.demoqa_page_locators.ELEMENTS_CARD)
        self.find(*self.demoqa_page_locators.ELEMENTS_CARD).click()

    def is_elements_page_header_visible(self):
        self.wait_for_element_to_appear(*self.demoqa_page_locators.ELEMENTS_PAGE_HEADER)
        elements_page_header = self.is_element_visible(*self.demoqa_page_locators.ELEMENTS_PAGE_HEADER)
        return elements_page_header
