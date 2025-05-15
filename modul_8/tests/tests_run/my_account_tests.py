import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, login_page, my_account_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_open_orders_tab(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        my_account_page.go_to_orders_tab(self.driver)
        self.assertTrue(my_account_page.orders_header_visible(self.driver))

    def test2_open_downloads_tab(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        my_account_page.go_to_downloads_tab(self.driver)
        self.assertTrue(my_account_page.downloads_header_visible(self.driver))

    def test3_open_address_tab(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        my_account_page.go_to_address_tab(self.driver)
        self.assertTrue(my_account_page.address_header_visible(self.driver))

    def test4_open_account_tab(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        my_account_page.go_to_my_account_tab(self.driver)
        self.assertTrue(my_account_page.my_account_header_visible(self.driver))

    def test5_log_out(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        my_account_page.logout_from_your_account(self.driver)
        self.assertTrue(login_page.login_page_header_visible(self.driver))



if __name__ == "__main__":
    unittest.main()