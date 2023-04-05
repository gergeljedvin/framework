#!/usr/bin/env python
from framework.base.base_tc import BaseTestCase
from framework.pages.google_page import GooglePage


class TestDummy(BaseTestCase):

    def setUp(self):
        super(TestDummy, self).setUp()

    def test_google_search(self):
        driver = self.driver

        # Google Search
        google_page = GooglePage(driver)

        # Is the Logo visible on the page
        self.assertTrue(google_page.is_logo_visible_on_the_page(),
                        "The Logo is not displayed!")

        google_page.enter_keyword_into_search_field_and_press_enter("QA-TEST")

    def tearDown(self):
        super(TestDummy, self).tearDown()
