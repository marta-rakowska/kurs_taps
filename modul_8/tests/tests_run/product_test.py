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
        pass

    def test6_add_review_without_test(self):
        pass

    def test7_add_review_without_username(self):
        pass

    def test8_add_review_without_email_address(self):
        pass






