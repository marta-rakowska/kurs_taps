from helpers.support_functions import *
from helpers.DataGenerator import *

order_confirmation_info = '//*[@id="post-8"]/div/div/div/p'


def order_confirmation_info_text_displayed(driver_instance):
    try:
        elem = wait_for_visibility_of_element(driver_instance, order_confirmation_info)
        value = 'Dziękujemy. Otrzymaliśmy Twoje zamówienie.'
        if elem.text == value:
            return True
    except StaleElementReferenceException:
        return False
