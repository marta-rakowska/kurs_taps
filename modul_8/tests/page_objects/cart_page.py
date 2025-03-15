from helpers.support_functions import *
from selenium.webdriver.support.select import Select


item_in_cart = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item_from_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]/a'
submit_cart = '//*[@id="post-7"]/div/div/div[2]/div/div/a'
coupon_code_input = '//*[@id="coupon_code"]'
apply_coupon_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[3]/td/div/button'
update_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/button'
cart_updated_alert = '//*[@id="post-7"]/div/div/div[1]/div'
quantity_input = '//*[@id="quantity_67cb5de23f9a1"]'
calculate_shipping_button = '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[2]/td/form/a'
shipping_country_dropdown = '//*[@id="select2-calc_shipping_country-container"]'
shipping_country_dropdown_list = '//*[@id="select2-calc_shipping_country-results"]'
shipping_city_input = '//*[@id="calc_shipping_city"]'
shipping_postcode_input = '//*[@id="calc_shipping_postcode"]'
update_shipping_button = '//*[@id="shipping-calculator-form"]/p[5]/button'

invalid_coupon = '123'
city = 'Jaworze'
postcode = '43-384'


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


def enter_coupon_code(driver_instance, coupon):
    wait_for_visibility_of_element(driver_instance, coupon_code_input)
    elem = driver_instance.find_element(By.XPATH, coupon_code_input)
    elem.send_keys(coupon)


def click_apply_coupon(driver_instance):
    wait_for_visibility_of_element(driver_instance, apply_coupon_button)
    elem = driver_instance.find_element(By.XPATH, apply_coupon_button)
    elem.click()


def update_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, update_cart_button)
    elem = driver_instance.find_element(By.XPATH, update_cart_button)
    elem.click()
    wait_for_invisibility_of_element(driver_instance, cart_updated_alert)
    elem2 = driver_instance.find_element(By.XPATH, cart_updated_alert)
    elem2.is_displayed()


def change_quantity_to_2(driver_instance):
    wait_for_visibility_of_element(driver_instance, quantity_input)
    elem = driver_instance.find_element(By.XPATH, quantity_input)
    elem.send_keys(2)


def click_calculate_shipping_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, calculate_shipping_button)
    elem = driver_instance.find_element(By.XPATH, calculate_shipping_button)
    elem.click()


def get_second_country_dropdown_value(driver_instance):
    wait_for_visibility_of_element(driver_instance, shipping_country_dropdown)
    elem_list = Select(driver_instance.find_element(By.XPATH, shipping_country_dropdown_list))
    wait_for_visibility_of_element(driver_instance, shipping_country_dropdown_list, time_to_wait=1)
    elem_list.select_by_index(10)


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


def calculate_shipping(driver_instance):
    click_calculate_shipping_button(driver_instance)
    get_second_country_dropdown_value(driver_instance)
    add_city(driver_instance)
    add_postcode(driver_instance)
    click_update_shipping_button()


def is_alert_present(driver_instance):
    try:
        driver_instance.switch_to.alert
    except NoAlertPresentException:
        return False












