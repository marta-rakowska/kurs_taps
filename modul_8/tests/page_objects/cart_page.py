from helpers.support_functions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


cart_page_header = '//*[@id="post-7"]/header/h1'
item_in_cart = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item_from_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]/a'
submit_cart = '//*[@id="post-7"]/div/div/div[2]/div/div/a'
coupon_code_input = '//*[@id="coupon_code"]'
apply_coupon_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button'
update_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/button'
cart_updated_alert = 'woocommerce-message'
quantity_input = '/html/body/div[1]/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[1]/td[5]/div/input'
calculate_shipping_button = '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[2]/td/form/a'
shipping_country_dropdown = '//*[@id="select2-calc_shipping_country-container"]'
shipping_country_dropdown_list = '//*[@id="select2-calc_shipping_country-results"]'
shipping_city_input = '//*[@id="calc_shipping_city"]'
shipping_postcode_input = '//*[@id="calc_shipping_postcode"]'
update_shipping_button = '//*[@id="shipping-calculator-form"]/p[5]/button'
items_in_cart_counter = '//*[@id="site-header-cart"]/li[1]/a/span[2]'
empty_cart_info = '//*[@id="post-7"]/div/div/div[2]/div'
back_to_shop_button = '//*[@id="post-7"]/div/div/p/a'
close_message_button = '/html/body/p/a'
shipping_cost_updated_info = '//*[@id="post-7"]/div/div/div[1]/div'


invalid_coupon = '123'
city = 'Jaworze'
postcode = '43-384'
number_of_items_in_cart = '2 Produkty'
coupon = 'fabrykatestow15'


def cart_page_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, cart_page_header)
    elem = driver_instance.find_element(By.XPATH, cart_page_header)
    header_text = 'Koszyk'
    if elem.text == header_text:
        return True
    else:
        return False


def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, item_in_cart)
    return elem.is_displayed()


def remove_item_from_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, remove_item_from_cart_button)
    elem.click()


def check_item_not_in_cart(driver_instance):
    try:
        wait_for_invisibility_of_element(driver_instance, item_in_cart)
        return True
    except NoSuchElementException:
        return False


def approve_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, submit_cart)
    elem.click()


def enter_coupon_code(driver_instance):
    wait_for_visibility_of_element(driver_instance, coupon_code_input)
    elem = driver_instance.find_element(By.XPATH, coupon_code_input)
    elem.send_keys(coupon)


def click_apply_coupon(driver_instance):
    wait_for_visibility_of_element(driver_instance, apply_coupon_button)
    elem = driver_instance.find_element(By.XPATH, apply_coupon_button)
    elem.click()


def change_quantity_to_2(driver_instance):
    elem = driver_instance.find_element(By.XPATH, quantity_input)
    # elem.clear()
    # elem.send_keys(2)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ENTER)


def cart_updated_alert_displayed(driver_instance):
    wait_for_visibility_of_element_by_class(driver_instance, cart_updated_alert)
    elem = driver_instance.find_element(By.CLASS_NAME, cart_updated_alert)
    alert_text = 'Koszyk zaktualizowany.'
    if alert_text in elem.text:
        return True
    else:
        return False


def click_calculate_shipping_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, calculate_shipping_button)
    elem = driver_instance.find_element(By.XPATH, calculate_shipping_button)
    elem.click()


def get_second_country_dropdown_value(driver_instance):
    wait_for_visibility_of_element(driver_instance, shipping_country_dropdown)
    elem_list = Select(driver_instance.find_element(By.XPATH, shipping_country_dropdown_list))
    wait_for_visibility_of_element(driver_instance, shipping_country_dropdown_list, time_to_wait=1)
    elem_list.select_by_index(2)


def add_city(driver_instance):
    wait_for_visibility_of_element(driver_instance, shipping_city_input)
    elem = driver_instance.find_element(By.XPATH, shipping_city_input)
    elem.send_keys(city)


def add_postcode(driver_instance):
    wait_for_visibility_of_element(driver_instance, shipping_postcode_input)
    elem = driver_instance.find_element(By.XPATH, shipping_postcode_input)
    elem.send_keys(postcode)


def click_update_shipping_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, update_shipping_button)
    elem = driver_instance.find_element(By.XPATH, update_shipping_button)
    elem.click()


def is_alert_present(driver_instance):
    try:
        driver_instance.switch_to.alert
    except NoAlertPresentException:
        return False


def check_number_of_items_in_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, number_of_items_in_cart)
    elem = driver_instance.find_element(By.XPATH, number_of_items_in_cart)
    if number_of_items_in_cart == elem.text:
        return True
    else:
        return False


def empty_cart_info_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, empty_cart_info)
    elem = driver_instance.find_element(By.XPATH, empty_cart_info)
    empty_cart_info_text = 'Twój koszyk aktualnie jest pusty.'
    if empty_cart_info_text in elem.text:
        return True
    else:
        return False


def go_back_to_shop(driver_instance):
    wait_for_visibility_of_element(driver_instance, back_to_shop_button)
    elem = driver_instance.find_element(By.XPATH, back_to_shop_button)
    elem.click()


def shipping_costs_updated_info_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, shipping_cost_updated_info)
    elem = driver_instance.find_element(By.XPATH, shipping_cost_updated_info)
    shipping_cost_updated_info_text = 'Koszty wysyłki zaktualizowane.'
    if shipping_cost_updated_info_text in elem.text:
        return True
    else:
        return False

















