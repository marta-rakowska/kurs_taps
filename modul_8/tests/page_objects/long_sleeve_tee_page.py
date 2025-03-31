from helpers.support_functions import *


product_page_header = '//*[@id="product-52"]/div[2]/h1'


def long_sleeve_tee_page_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, product_page_header)
    elem = driver_instance.find_element(By.XPATH, product_page_header)
    product_name = 'Long Sleeve Tee'
    if elem.text == product_name:
        return True
    else:
        return False
