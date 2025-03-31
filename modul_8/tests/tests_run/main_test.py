import time
import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, cart_page, invalid_page, login_page, long_sleeve_tee_page, shop_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_go_to_cart_page(self):
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.cart_page_header_visible(self.driver))

    def test2_go_to_my_account(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.login_page_header_visible(self.driver))

    def test3_go_to_shop_page(self):
        main_page.go_to_shop_page(self.driver)
        self.assertTrue(shop_page.shop_page_header_visible(self.driver))

    def test4_go_to_invalid_page(self):
        main_page.go_to_invalid_page(self.driver)
        self.assertTrue(invalid_page.error_info_displayed(self.driver))

    def test5_search_for_valid_product(self):
        main_page.search_for_valid_product(self.driver)
        self.assertTrue(long_sleeve_tee_page.long_sleeve_tee_page_header_visible(self.driver))

    def test6_search_for_invalid_product(self):
        main_page.search_for_invalid_product(self.driver)
        self.assertTrue(main_page.no_products_found_info_displayed(self.driver))









