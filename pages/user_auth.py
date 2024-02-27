from selenium.webdriver import ActionChains
from locators.locators import Headers
from locators.locators import Auth
from locators.locators import Restore
from pages.base_page import BasePage
import allure


class UserAuth(BasePage):
    @allure.step('Авторизация пользователя')
    def user_auth(self, user_login, user_password):
        # переход по клику на «Личный кабинет»
        skip_modal_and_go_login = self.find_element_located(Headers.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        self.find_element_to_be_clickable(Auth.login_field)
        self.find_element_to_be_clickable(Auth.password_field)
        self.find_element_located(Auth.login_field).send_keys(user_login)
        self.find_element_located(Auth.password_field).send_keys(user_password)
        self.find_element_located_click(Auth.accept_login_button)

    @allure.step('Проверка перехода в историю и выход из аккаунта')
    def check_history_list(self):
        skip_modal_and_go_login = self.find_element_located(Headers.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        # Переход в раздел «История заказов»
        self.find_element_located_click(Auth.history_button)
        # Выход из аккаунта
        self.find_element_located_click(Auth.logout_button)
        self.find_element_located(Restore.restore_button)
