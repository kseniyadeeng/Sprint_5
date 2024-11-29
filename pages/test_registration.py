import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import *
from urls import Urls
from data import PersonData
from data import ValidData

class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        # При успешной регистрации переход на страницу входа
        driver.get(Urls.url_register)
        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)
        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_element_with_login_text))
        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'


    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        # При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'
        driver.get(Urls.url_register)
        driver.find_element(*AuthRegistre.ar_name_field).send_keys(PersonData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password_list)
        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistre.ar_error_message))
        error_message = driver.find_element(*AuthRegistre.ar_error_message)
        assert error_message.text == 'Некорректный пароль'
