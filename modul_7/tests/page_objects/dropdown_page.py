from helpers.support_functions import *
from selenium.webdriver.support.select import Select

dropdown_tab = '//*[@id="dropdownlist-header"]'
dropdown_content = '//*[@id="dropdownlist-content"]'
dropdown_list = '//*[@id="dropdown"]'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, dropdown_tab)
    elem.click()


def dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dropdown_content)
    return elem.is_displayed()


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element(By.XPATH, dropdown_list))
    wait_for_visibility_of_element(driver_instance, dropdown_list, time_to_wait=1)
    elem_list.select_by_index(1)



