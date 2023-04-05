#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from framework.base.base_page import BasePage, GenericLocators


class BaseDialogLocators(object):

    """
        Container fo Dialog base locators for elements that are universally present on dialogs
    """

    # locators that all dialogs have


class BaseDialog(BasePage):

    """
        Container for base functions to interact with Dialogs
    """

    def __init__(self, driver):
        super(BaseDialog, self).__init__(driver)
        self.driver = driver
        self.base_dialog_locators = BaseDialogLocators
        self.generic_locators = GenericLocators


