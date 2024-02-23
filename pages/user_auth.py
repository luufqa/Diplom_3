from selenium.webdriver import ActionChains
from locators.locators import Locators
from pages.base_page import BasePage
import allure
import time


class UserAuth(BasePage):
    @allure.step('Авторизация пользователя')
    def user_auth(self):
        # переход по клику на «Личный кабинет»
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        time.sleep(5)
        self.find_element_located(Locators.login_field).send_keys(Locators.user_email)
        self.find_element_located(Locators.password_field).send_keys(Locators.user_password)
        self.find_element_located_click(Locators.accept_login_button)

    @allure.step('Проверка перехода в историю и выход из аккаунта')
    def check_history_list(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        # Переход в раздел «История заказов»
        self.find_element_located_click(Locators.history_button)
        # Выход из аккаунта
        self.find_element_located_click(Locators.logout_button)
        self.find_element_located(Locators.restore_button)
