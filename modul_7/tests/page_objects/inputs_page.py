from helpers.support_functions import *

input_tab = '//*[@id="inputs-header"]'
input_content = '//*[@id="inputs-content"]'
input = '//*[@id="inputs-content"]/div/input'


def click_inputs_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, input_tab)
    elem.click()


def input_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, input_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, input)
    elem.send_keys('123456')
    value = '123456'
    if value == elem.get_attribute('value'):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, input)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True



