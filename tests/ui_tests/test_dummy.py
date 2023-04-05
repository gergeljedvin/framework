#!/usr/bin/env python
from framework.base.base_tc import BaseTestCase
from framework.pages.demoqa_page import DemoqaPage


class TestDummy(BaseTestCase):

    def setUp(self):
        super(TestDummy, self).setUp()

    def test_google_search(self):
        driver = self.driver

        # Google Search
        demoqa_page = DemoqaPage(driver)

        # Is the Logo visible on the page
        self.assertTrue(demoqa_page.is_logo_visible_on_the_page(),
                        "The Logo is not displayed!")

        # Is the Elements card visible on the page
        self.assertTrue(demoqa_page.is_elements_card_visible_on_the_page(),
                        "The Elements card is not displayed!")

        # Click on the Elements card
        demoqa_page.click_on_the_elements_card()

        # Is the Elements page header visible on the page
        self.assertTrue(demoqa_page.is_elements_page_header_visible(),
                        "The header on the Elements page is not displayed!")

    def tearDown(self):
        super(TestDummy, self).tearDown()
