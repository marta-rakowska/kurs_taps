from helpers.support_functions import *
from selenium.webdriver.support.select import Select
from helpers.DataGenerator import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


order_page_header = '//*[@id="post-8"]/header/h1'
name = '//*[@id="billing_first_name"]'
surname = '//*[@id="billing_last_name"]'
dropdown_country = '//*[@id="billing_country"]'
street = '//*[@id="billing_address_1"]'
postcode = '//*[@id="billing_postcode"]'
city = '//*[@id="billing_city"]'
phone = '//*[@id="billing_phone"]'
email = '//*[@id="billing_email"]'
place_order_button = 'place_order'
show_login_button = '//*[@id="post-8"]/div/div/div[2]/div/a'
username_input = '//*[@id="username"]'
password_input = '//*[@id="password"]'
login_button = '//*[@id="post-8"]/div/div/form[1]/p[4]/button'
show_coupon_button = '//*[@id="post-8"]/div/div/div[3]/div/a'
coupon_input = '//*[@id="coupon_code"]'
apply_coupon_button = 'apply_coupon'
missing_data_info = '//*[@id="post-8"]/div/div/form[3]/div[1]/div/ul/li/a'
store_notice = '/html/body/p/a'
incorrect_username_or_password_error = '//*[@id="post-8"]/div/div/div[1]/ul/li/span'


valid_postcode = '00-123'
invalid_postcode = 'abc'

proper_email = 'cotaga1249@maillei.net'
proper_password = 'VRrMhK8MqFyd'

wrong_password = 'wrongpassword123'
invalid_coupon = 'invalidcoupon'


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
    WebDriverWait(driver_instance, 5).until(EC.staleness_of(driver_instance.find_element(By.ID, place_order_button)))
    elem = driver_instance.find_element(By.ID, place_order_button)
    elem.click()


def wrong_email_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Nieprawidłowy adres e-mail płatności'
    if alert_text in elem.text:
        return True
    else:
        return False


def wrong_phone_number_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Nieprawidłowy adres e-mail płatności'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_name_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Imię płatnika'
    if alert_text in elem.text:
        print(elem.text)
        return True
    else:
        return False


def missing_surname_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Nazwisko płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_street_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Ulica płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_postcode_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Kod pocztowy płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_city_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Miasto płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_phone_number_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Numer telefonu płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def missing_email_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, missing_data_info)
    elem = driver_instance.find_element(By.XPATH, missing_data_info)
    alert_text = 'Adres e-mail płatnika'
    if alert_text in elem.text:
        return True
    else:
        return False


def click_show_login_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, show_login_button)
    elem = driver_instance.find_element(By.XPATH, show_login_button)
    elem.click()


def click_show_coupon_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, show_coupon_button)
    elem = driver_instance.find_element(By.XPATH, show_coupon_button)
    elem.click()


def login_section_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input)
    elem = driver_instance.find_element(By.XPATH, username_input)
    return elem.is_displayed()


def coupon_section_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, coupon_input)
    elem = driver_instance.find_element(By.XPATH, coupon_input)
    return elem.is_displayed()


def enter_correct_username(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input)
    elem = driver_instance.find_element(By.XPATH, username_input)
    elem.send_keys(proper_email)


def enter_incorrect_username(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input)
    elem = driver_instance.find_element(By.XPATH, username_input)
    elem.send_keys(DataGenerator.generateWrongEmail())


def enter_correct_password(driver_instance):
    elem = driver_instance.find_element(By.XPATH, password_input)
    elem.send_keys(proper_password)


def enter_incorrect_password(driver_instance):
    elem = driver_instance.find_element(By.XPATH, password_input)
    elem.send_keys(wrong_password)


def enter_incorrect_coupon(driver_instance):
    elem = driver_instance.find_element(By.XPATH, coupon_input)
    elem.send_keys(invalid_coupon)


def click_login_button(driver_instance):
    elem = driver_instance.find_element(By.XPATH, login_button)
    elem.click()


def click_apply_coupon_button(driver_instance):
    elem = driver_instance.find_element(By.NAME, 'apply_coupon')
    elem.click()


def incorrect_username_or_password_error_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, incorrect_username_or_password_error)
    elem = driver_instance.find_element(By.XPATH, incorrect_username_or_password_error)
    alert_text = 'nieprawidłowa nazwa użytkownika lub hasło'
    if alert_text in elem.text:
        return True
    else:
        return False































