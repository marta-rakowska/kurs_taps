import time
import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, cart_page, order_page, order_confirmation_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_confirmation_page.order_confirmation_page_header_displayed(self.driver))


if __name__ == "__main__":
    unittest.main()
