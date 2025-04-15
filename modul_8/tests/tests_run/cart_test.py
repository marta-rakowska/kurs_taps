import time
import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, cart_page, shop_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_add_item_to_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test2_remove_item_from_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_item_not_in_cart(self.driver))

    def test3_change_amount_to_2(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.change_quantity_to_2(self.driver)
        self.assertTrue(cart_page.cart_updated_alert_displayed(self.driver))

    def test5_calculate_shipping(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.click_calculate_shipping_button(self.driver)
        cart_page.add_city(self.driver)
        cart_page.add_postcode(self.driver)
        cart_page.click_update_shipping_button(self.driver)
        cart_page.shipping_costs_updated_info_displayed(self.driver)

    def test6_empty_cart_info_displayed(self):
        main_page.go_to_cart_page(self.driver)
        cart_page.empty_cart_info_displayed(self.driver)

    def test7_go_back_to_shop(self):
        main_page.go_to_cart_page(self.driver)
        cart_page.go_back_to_shop(self.driver)
        shop_page.shop_page_header_visible(self.driver)


if __name__ == "__main__":
    unittest.main()
