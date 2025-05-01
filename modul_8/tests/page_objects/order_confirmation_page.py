from helpers.support_functions import *
from helpers.DataGenerator import *
from selenium.common.exceptions import StaleElementReferenceException

# order_confirmation_page_header = '//*[@id="post-8"]/header/h1'
order_confirmation_page_header = 'entry-title'


def order_confirmation_page_header_displayed(driver_instance):
    try:
        WebDriverWait(driver_instance, 5).until(
            EC.staleness_of(driver_instance.find_element(By.CLASS_NAME, order_confirmation_page_header)))
        elem = driver_instance.find_element(By.CLASS_NAME, order_confirmation_page_header)
        value = 'Zamówienie otrzymane'
        if value in elem.text:
            return True
    except StaleElementReferenceException:
        return False
