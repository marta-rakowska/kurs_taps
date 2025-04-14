import time
import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, shop_page, beanie_product_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_go_to_additional_info_tab(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_additional_information_tab(self.driver)
        self.assertTrue(beanie_product_page.additional_information_tab_header_visible(self.driver))

    def test2_go_to_reviews_tab(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        self.assertTrue(beanie_product_page.reviews_tab_header_visible(self.driver))

    def test3_add_correct_review(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_valid_review(self.driver)
        self.assertTrue(beanie_product_page.added_comment_visible(self.driver))

    def test5_add_review_without_rating(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_review_without_rating(self.driver)
        self.assertTrue(beanie_product_page.missing_rating_alert_displayed(self.driver))

    def test6_add_review_without_text(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_review_without_text(self.driver)
        self.assertTrue(beanie_product_page.add_review_error_message_visible(self.driver))

    def test7_add_review_without_author(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_review_without_author_name(self.driver)
        self.assertTrue(beanie_product_page.add_review_error_message_visible(self.driver))

    def test8_add_review_without_email(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_review_without_author_email(self.driver)
        self.assertTrue(beanie_product_page.add_review_error_message_visible(self.driver))

    def test_9_add_empty_review(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.go_to_reviews_tab(self.driver)
        beanie_product_page.add_empty_review(self.driver)
        self.assertTrue(beanie_product_page.missing_rating_alert_displayed(self.driver))

    def test_10_add_2_products_to_cart(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        beanie_product_page.change_quantity_to_2(self.driver)
        beanie_product_page.add_to_cart(self.driver)
        self.assertTrue(beanie_product_page.two_products_added_to_cart_info_displayed(self.driver))











