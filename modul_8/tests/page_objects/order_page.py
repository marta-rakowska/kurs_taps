from helpers.support_functions import *
from selenium.webdriver.support.select import Select
from helpers.DataGenerator import *


order_page_header = '//*[@id="post-8"]/header/h1'
name = '//*[@id="billing_first_name"]'
surname = '//*[@id="billing_last_name"]'
dropdown_country = '//*[@id="billing_country"]'
street = '//*[@id="billing_address_1"]'
postcode = '//*[@id="billing_postcode"]'
city = '//*[@id="billing_city"]'
phone = '//*[@id="billing_phone"]'
email = '//*[@id="billing_email"]'
place_order_button = '//*[@id="place_order"]'
show_login_button = '//*[@id="post-8"]/div/div/div[2]/div/a'
username_input = '//*[@id="username"]'
password_input = '//*[@id="password"]'
login_button = '//*[@id="post-8"]/div/div/form[1]/p[4]/button'
show_coupon_button = '//*[@id="post-8"]/div/div/div[3]/div/a'
coupon_input = '//*[@id="coupon_code"]'
submit_coupon_button = '//*[@id="post-8"]/div/div/form[2]/p[3]/button'
missing_data_info = '//*[@id="post-8"]/div/div/form[3]/div[1]/div/ul/li/a'

valid_postcode = '00-123'
invalid_postcode = 'abc'

proper_email = 'cotaga1249@maillei.net'
proper_password = 'VRrMhK8MqFyd'


def order_page_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, order_page_header)
    elem = driver_instance.find_element(By.XPATH, order_page_header)
    header_text = 'Zamówienie'
    if elem.text == header_text:
        return True
    else:
        return False


def form_add_proper_name(driver_instance):
    elem = driver_instance.find_element(By.XPATH, name)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_name(driver_instance):
    elem = driver_instance.find_element(By.XPATH, name)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_surname(driver_instance):
    elem = driver_instance.find_element(By.XPATH, surname)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_surname(driver_instance):
    elem = driver_instance.find_element(By.XPATH, surname)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element(By.XPATH, dropdown_country))
    wait_for_visibility_of_element(driver_instance, dropdown_country, time_to_wait=1)
    elem_list.select_by_index(1)


def form_add_proper_street(driver_instance):
    elem = driver_instance.find_element(By.XPATH, street)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_street(driver_instance):
    elem = driver_instance.find_element(By.XPATH, street)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_city(driver_instance):
    elem = driver_instance.find_element(By.XPATH, city)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_city(driver_instance):
    elem = driver_instance.find_element(By.XPATH, city)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_postcode(driver_instance):
    elem = driver_instance.find_element(By.XPATH, postcode)
    elem.send_keys(valid_postcode)


def form_add_wrong_postcode(driver_instance):
    elem = driver_instance.find_element(By.XPATH, postcode)
    elem.send_keys(invalid_postcode)


def form_add_proper_phone(driver_instance):
    elem = driver_instance.find_element(By.XPATH, phone)
    elem.send_keys(DataGenerator.generateProperMobileNumber(DataGenerator()))


def form_add_wrong_phone(driver_instance):
    elem = driver_instance.find_element(By.XPATH, phone)
    elem.send_keys(DataGenerator.generateWrongMobileNumber(DataGenerator()))


def form_add_proper_email(driver_instance):
    elem = driver_instance.find_element(By.XPATH, email)
    elem.send_keys(DataGenerator.generateProperEmail())


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element(By.XPATH, email)
    elem.send_keys(DataGenerator.generateWrongEmail())


def proper_fill_all_form_areas(driver_instance):
    form_add_proper_name(driver_instance)
    form_add_proper_surname(driver_instance)
    get_first_dropdown_value(driver_instance)
    form_add_proper_street(driver_instance)
    form_add_proper_city(driver_instance)
    form_add_proper_postcode(driver_instance)
    form_add_proper_phone(driver_instance)
    form_add_proper_email(driver_instance)


def submit_order(driver_instance):
    wait_for_visibility_of_element(driver_instance, place_order_button, time_to_wait=3)
    elem = driver_instance.find_element(By.XPATH, place_order_button)
    elem.click()














