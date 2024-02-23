from selenium.webdriver import ActionChains
from locators.locators import Locators
from pages.base_page import BasePage
import allure
import time


class RestorePassword(BasePage):
    @allure.step('Восстановление пароля и проверка активного поля(через глазик)')
    def restore_password(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        # Переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        self.find_element_located_click(Locators.restore_button)
        # Ввод почты и клик по кнопке «Восстановить»
        self.find_element_located(Locators.restore_input_email).send_keys(Locators.user_email)
        # Здесь необходим time, т.к. сайт тормозит (не успевает кнопку найти)
        time.sleep(6)
        self.find_element_located_click(Locators.accept_restore_button)
        # Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
        skip_modal_and_go_visible = self.find_element_located(Locators.visible_password)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_visible).click().perform()
        result = self.find_element_located(Locators.change_active_field).get_attribute('class')
        return result
