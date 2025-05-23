import unittest
from selenium import webdriver
from modul_8.config.test_settings import TestSettings
from modul_8.tests.page_objects import main_page, login_page, lost_password_page, my_account_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_logo_visible(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))

    def test2_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(my_account_page.my_account_header_visible(self.driver))

    def test3_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.incorrect_login(self.driver)
        self.assertTrue(login_page.wrong_user_or_password_error_displayed(self.driver))

    def test4_remind_password(self):
        main_page.go_to_login_page(self.driver)
        login_page.go_to_lost_password_page(self.driver)
        self.assertTrue(lost_password_page.lost_password_header_visible(self.driver))
        lost_password_page.reset_password(self.driver)
        self.assertTrue(lost_password_page.password_reset_alert_visible(self.driver))

    def test5_register_new_user(self):
        main_page.go_to_login_page(self.driver)
        login_page.register_new_user(self.driver)
        self.assertTrue(my_account_page.my_account_header_visible(self.driver))


if __name__ == "__main__":
    unittest.main()
