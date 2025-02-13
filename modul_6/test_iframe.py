import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from modul_6 import iframe_page


class Tests(unittest.TestCase):

    def setUp(self):
        chromedriver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"chromedriver")
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('http://simpletestsite.fabrykatestow.pl/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_iframe_visibility(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test2_iframe_click_first_button(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe(self.driver))