from helpers.support_functions import *


hoodie_page_header = '//*[@id="product-43"]/div[2]/h1'
out_of_stock_info = '//*[@id="product-43"]/div[2]/form/p'

out_of_stock_info_text = 'Tego produktu nie ma na stanie i nie jest dostępny.'


def hoodie_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, hoodie_page_header)
    elem = driver_instance.find_element(By.XPATH, hoodie_page_header)
    header_text = 'Hoodie'
    if elem.text == header_text:
        return True
    else:
        return False


def out_of_stock_info_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, out_of_stock_info)
    elem = driver_instance.find_element(By.XPATH, out_of_stock_info)
    if elem.text == out_of_stock_info_text:
        return True
    else:
        return False
    
