from helpers.support_functions import *

lost_password_header = '//*[@id="post-9"]/header/h1'
user_login_input = '//*[@id="user_login"]'
user_login = 'xirawep342@framitag.com'
reset_password_button = '//*[@id="post-9"]/div/div/form/p[3]/button'
password_reset_alert = '//*[@id="post-9"]/div/div/div'


def my_account_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, lost_password_header)
    elem = driver_instance.find_element(By.XPATH, lost_password_header)
    header_text = 'Zapomniane hasło'
    if elem.text == header_text:
        return True
    else:
        return False


def reset_password(driver_instance):
    wait_for_visibility_of_element(driver_instance, user_login_input)
    elem = driver_instance.find_element(By.XPATH, user_login_input)
    elem.send_keys(user_login)


def password_reset_alert_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, password_reset_alert)
    return elem.is_displayed()





