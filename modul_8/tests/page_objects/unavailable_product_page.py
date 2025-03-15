from helpers.support_functions import *


out_of_stock_info = '//*[@id="product-43"]/div[2]/form/p'


out_of_stock_info_text = 'Tego produktu nie ma na stanie i nie jest dostępny.'


def out_of_stock_info_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, out_of_stock_info)
    elem = driver_instance.find_element(By.XPATH, out_of_stock_info)
    if elem.text == out_of_stock_info_text:
        return True
    else:
        return False
    
