from helpers.support_functions import *

error_info = '//*[@id="post-1565"]/div/p[1]'
back_to_main_page_button = '//*[@id="post-1565"]/div/div[2]/div/a'


def error_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, error_info)
    return elem.is_displayed()


def go_to_main_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, back_to_main_page_button)
    elem = driver_instance.find_element(By.XPATH, back_to_main_page_button)
    elem.click()

