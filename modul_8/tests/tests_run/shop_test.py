import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, shop_page, beanie_product_page, hoodie_product_page
import time


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_go_to_beanie_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_beanie_page(self.driver)
        self.assertTrue(beanie_product_page.beanie_header_visible(self.driver))

    def test2_go_to_hoodie_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_hoodie_page(self.driver)
        self.assertTrue(hoodie_product_page.hoodie_header_visible(self.driver))

    def test3_go_to_next_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_next_page(self.driver)
        self.assertTrue(shop_page.second_page_visible(self.driver))

    def test4_go_to_previous_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_next_page(self.driver)
        shop_page.go_to_previous_page(self.driver)
        self.assertTrue(shop_page.first_page_visible(self.driver))

    def test3_go_to_second_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_second_page(self.driver)
        self.assertTrue(shop_page.second_page_visible(self.driver))

    def test4_go_to_first_page(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_second_page(self.driver)
        shop_page.go_to_first_page(self.driver)
        self.assertTrue(shop_page.first_page_visible(self.driver))