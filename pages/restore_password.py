from selenium.webdriver import ActionChains
from locators.locators import Headers
from locators.locators import Restore
from pages.base_page import BasePage
import allure


class RestorePassword(BasePage):
    @allure.step('Восстановление пароля и проверка активного поля(через глазик)')
    def restore_password(self, user_login):
        skip_modal_and_go_login = self.find_element_located(Headers.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        # Переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        self.find_element_located_click(Restore.restore_button)
        # Ввод почты и клик по кнопке «Восстановить»
        self.find_element_located(Restore.restore_input_email).send_keys(user_login)
        self.find_element_to_be_clickable(Restore.accept_restore_button)
        self.find_element_located_click(Restore.accept_restore_button)
        # Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
        skip_modal_and_go_visible = self.find_element_located(Restore.visible_password)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_visible).click().perform()
        result = self.find_element_located(Restore.change_active_field).get_attribute('class')
        return result
