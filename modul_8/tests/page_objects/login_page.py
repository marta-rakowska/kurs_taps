from helpers.support_functions import *
from helpers.DataGenerator import *

login_page_header = '//*[@id="post-9"]/header/h1'
username = '//*[@id="username"]'
password = '//*[@id="password"]'
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
close_message_button = '/html/body/p/a'
random_password = 'test'
error_info = '//*[@id="content"]/div/div[1]/ul'
lost_password_button = '//*[@id="customer_login"]/div[1]/form/p[4]/a'
email = '//*[@id="reg_email"]'
register_button = '//*[@id="customer_login"]/div[2]/form/p[3]/button'


proper_email1 = 'cotaga1249@maillei.net'
proper_password1 = 'VRrMhK8MqFyd'

proper_email2 = 'wowen49501@maillei.net'
proper_password2 = 'lxsg#GAqH$Ke'

proper_email3 = 'bomineg967@onmail3.com'
proper_password3 = 'zedvu@##)CZy'

proper_email4 = 'wacog70401@tinkmail.net'
proper_password4 = 'Lk*3Q9&am3zL'

proper_email5 = 'calose2528@maillei.net'
proper_password5 = 'lkSb&SAJwLWo'


def login_page_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, login_page_header)
    elem = driver_instance.find_element(By.XPATH,login_page_header)
    header_text = 'Moje konto'
    if elem.text == header_text:
        return True
    else:
        return False


def correct_login(driver_instance):
    elem = driver_instance.find_element(By.XPATH, username)
    elem.send_keys(proper_email1)
    elem1 = driver_instance.find_element(By.XPATH, password)
    elem1.send_keys(proper_password1)
    elem2 = driver_instance.find_element(By.XPATH, close_message_button)
    elem2.click()
    elem3 = driver_instance.find_element(By.XPATH, login_button)
    elem3.click()


def incorrect_login(driver_instance):
    elem = driver_instance.find_element(By.XPATH, username)
    elem.send_keys(DataGenerator.generateWrongEmail())
    elem1 = driver_instance.find_element(By.XPATH, password)
    elem1.send_keys(random_password)
    elem2 = driver_instance.find_element(By.XPATH, close_message_button)
    elem2.click()
    elem3 = driver_instance.find_element(By.XPATH, login_button)
    elem3.click()


def wrong_user_or_password_error_displayed(driver_instance):
    try:
        wait_for_visibility_of_element(driver_instance, error_info)
        elem = driver_instance.find_element(By.XPATH, error_info)
        return elem.is_displayed()
    except StaleElementReferenceException:
        print('ERROR Wrong user/password')
        return True


def go_to_lost_password_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, close_message_button)
    elem.click()
    wait_for_visibility_of_element(driver_instance, lost_password_button)
    elem2 = driver_instance.find_element(By.XPATH, lost_password_button)
    elem2.click()


def register_new_user(driver_instance):
    elem = driver_instance.find_element(By.XPATH, close_message_button)
    elem.click()
    wait_for_visibility_of_element(driver_instance, email)
    elem2 = driver_instance.find_element(By.XPATH, email)
    elem2.send_keys(DataGenerator.generateProperEmail())
    elem3 = driver_instance.find_element(By.XPATH, register_button)
    elem3.click()













