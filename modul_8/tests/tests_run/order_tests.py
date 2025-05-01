import time
import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, cart_page, order_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_open_login_section(self):
        pass

    def test2_correct_login(self):
        pass

    def test3_incorrect_login(self):
        pass

    def test4_open_coupon_section(self):
        pass

    def test5_add_incorrect_coupon(self):
        pass

    def test6_submit_order_without_name(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_name_alert_displayed(self.driver))

    def test7_submit_order_without_surname(self):
        pass

    def test8_submit_order_without_street(self):
        pass

    def test9_submit_order_without_post_code(self):
        pass

    def test10_submit_order_without_city(self):
        pass

    def test11_submit_order_without_phone_number(self):
        pass

    def test12_submit_order_without_email(self):
        pass
