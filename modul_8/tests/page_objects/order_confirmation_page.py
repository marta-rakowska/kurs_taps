from helpers.support_functions import *
from helpers.DataGenerator import *
from selenium.common.exceptions import StaleElementReferenceException

order_confirmation_page_header = '//*[@id="post-8"]/header/h1'


def order_confirmation_page_header_displayed(driver_instance):
    try:
        wait_for_visibility_of_element(driver_instance, order_confirmation_page_header)
        elem = driver_instance.find_element(By.XPATH, order_confirmation_page_header)
        value = 'Zamówienie otrzymane'
        if value in elem.text:
            return True
    except StaleElementReferenceException:
        return False
