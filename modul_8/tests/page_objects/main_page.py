from helpers.support_functions import *

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_page_header_link = '//*[@id="menu-item-100"]/a'
cart_page_header_link = '//*[@id="menu-item-99"]/a'
add_hoodie_to_cart = '//*[@id="post-83"]/div/div[4]/ul/li[3]/div[2]/a'
go_to_cart_under_item = '//*[@id="post-83"]/div/div[4]/ul/li[3]/div[2]/a[2]'
cart_button_header = '//*[@id="site-header-cart"]'
close_message_button = '/html/body/p/a'


def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, taps_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_page_header_link)
    elem = driver_instance.find_element(By.XPATH, my_account_page_header_link)
    elem.click()


def add_item_to_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, close_message_button)
    elem.click()
    elem2 = driver_instance.find_element(By.XPATH, add_hoodie_to_cart)
    elem2.click()


def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, go_to_cart_under_item)
    elem = driver_instance.find_element(By.XPATH, go_to_cart_under_item)
    elem.click()




