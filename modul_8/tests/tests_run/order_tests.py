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
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.click_show_login_button(self.driver)
        self.assertTrue(order_page.login_section_displayed(self.driver))

    def test2_correct_login(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.click_show_login_button(self.driver)
        order_page.enter_correct_username(self.driver)
        order_page.enter_correct_password(self.driver)
        order_page.click_login_button(self.driver)

    def test3_login_with_incorrect_username(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.click_show_login_button(self.driver)
        order_page.enter_incorrect_username(self.driver)
        order_page.enter_correct_password(self.driver)
        order_page.click_login_button(self.driver)
        self.assertTrue(order_page.incorrect_username_or_password_error_displayed(self.driver))

    def test4_login_with_incorrect_password(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.click_show_login_button(self.driver)
        order_page.enter_correct_username(self.driver)
        order_page.enter_incorrect_password(self.driver)
        order_page.click_login_button(self.driver)
        self.assertTrue(order_page.incorrect_username_or_password_error_displayed(self.driver))

    def test5_open_coupon_section(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.click_show_coupon_button(self.driver)
        self.assertTrue(order_page.coupon_section_displayed(self.driver))

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
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_surname_alert_displayed(self.driver))

    def test8_submit_order_without_street(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_street_alert_displayed(self.driver))

    def test9_submit_order_without_postcode(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_postcode_alert_displayed(self.driver))

    def test10_submit_order_without_city(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_city_alert_displayed(self.driver))

    def test11_submit_order_without_phone_number(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_email(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_phone_number_alert_displayed(self.driver))

    def test12_submit_order_without_email(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_under_item(self.driver)
        cart_page.approve_cart(self.driver)
        order_page.form_add_proper_name(self.driver)
        order_page.form_add_proper_surname(self.driver)
        order_page.form_add_proper_street(self.driver)
        order_page.form_add_proper_postcode(self.driver)
        order_page.form_add_proper_city(self.driver)
        order_page.form_add_proper_phone(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.missing_email_alert_displayed(self.driver))


if __name__ == "__main__":
    unittest.main()
