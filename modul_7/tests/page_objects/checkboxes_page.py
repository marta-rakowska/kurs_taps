from helpers.support_functions import *

checkbox_tab = '//*[@id="checkbox-header"]'
all_checkboxes = '//*[@id="checkboxes"]'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def checkboxes_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, all_checkboxes)
    return elem.is_displayed()


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, checkbox_tab)
    elem = driver_instance.find_element(By.XPATH, checkbox_tab)
    elem.click()


def click_checkboxes(driver_instance):
    elem = driver_instance.find_element(By.XPATH, checkbox_1)
    elem.click()
    elem1 = driver_instance.find_element(By.XPATH, checkbox_2)
    elem1.click()



