import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl'
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        checkboxes_tab = self.driver.find_element(By.ID, 'checkbox-header')
        checkboxes_tab.click()
        time.sleep(1)
        checkbox_2 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
        checkbox_2.click()
        time.sleep(1)
        self.driver.save_screenshot('screenshot.png')



