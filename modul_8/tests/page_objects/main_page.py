from helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_button_header = '//*[@id="menu-item-100"]/a'
cart_page_button_header = '//*[@id="menu-item-99"]/a'
add_hoodie_to_cart = '//*[@id="post-83"]/div/div[4]/ul/li[3]/div[2]/a'
cart_under_item = '//*[@id="post-83"]/div/div[4]/ul/li[3]/div[2]/a[2]'
cart_button_header = '//*[@id="site-header-cart"]/a'
close_message_button = '/html/body/p/a'
order_button_header = '//*[@id="menu-item-101"]/a'
shop_button_header = '//*[@id="menu-item-102"]/a'
oh_no_button_header = '//*[@id="menu-item-1568"]/a'
search_field = '//*[@id="woocommerce-product-search-field-0"]'
no_products_found_info = '//*[@id="main"]/div/div'


valid_product_name = 'Long Sleeve Tee'
invalid_product_name = 'Anorak'


def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, taps_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_button_header)
    elem = driver_instance.find_element(By.XPATH, my_account_button_header)
    elem.click()


def add_item_to_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, close_message_button)
    elem.click()
    elem2 = driver_instance.find_element(By.XPATH, add_hoodie_to_cart)
    elem2.click()


def go_to_cart_under_item(driver_instance):
    wait_for_visibility_of_element(driver_instance, cart_under_item)
    elem = driver_instance.find_element(By.XPATH, cart_under_item)
    elem.click()


def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, cart_page_button_header)
    elem = driver_instance.find_element(By.XPATH, cart_page_button_header)
    elem.click()


def go_to_order_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, order_button_header)
    elem = driver_instance.find_element(By.XPATH, order_button_header)
    elem.click()


def go_to_shop_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, shop_button_header)
    elem = driver_instance.find_element(By.XPATH, shop_button_header)
    elem.click()


def go_to_invalid_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, oh_no_button_header)
    elem = driver_instance.find_element(By.XPATH, oh_no_button_header)
    elem.click()


def search_for_valid_product(driver_instance):
    wait_for_visibility_of_element(driver_instance, search_field)
    elem = driver_instance.find_element(By.XPATH, search_field)
    elem.send_keys(valid_product_name)
    elem.send_keys(Keys.ENTER)


def search_for_invalid_product(driver_instance):
    wait_for_visibility_of_element(driver_instance, search_field)
    elem = driver_instance.find_element(By.XPATH, search_field)
    elem.send_keys(invalid_product_name)
    elem.send_keys(Keys.ENTER)


def no_products_found_info_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, no_products_found_info)
    elem = driver_instance.find_element(By.XPATH, no_products_found_info)
    info_text = 'Nie znaleziono produktów, których szukasz.'
    if info_text in elem.text:
        return True
    else:
        return False















