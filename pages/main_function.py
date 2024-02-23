from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from pages.base_page import BasePage
import allure
import time


class MainFunction(BasePage):
    @allure.step('Создание нового заказа')
    def main_function(self):
        # Переход в меню Конструктор
        skip_modal_and_go_constructor = self.find_element_located(Locators.constructor)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_constructor).click().perform()
        # Переход в меню Лента заказов
        skip_modal_and_go_feed = self.find_element_located(Locators.feed)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_feed).click().perform()
        ActionChains(self.driver).move_to_element(skip_modal_and_go_constructor).click().perform()
        # Если кликнуть на ингредиент, появится всплывающее окно с деталями
        skip_modal_and_go_first_ingr = self.find_element_located(Locators.first_ingredient)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_first_ingr).click().perform()
        # Всплывающее окно закрывается кликом по крестику
        self.find_element_located_click(Locators.close_modal)
        # При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается
        drag = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.first_ingredient))
        drop = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.field_for_order))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        self.find_element_located_click(Locators.accept_order_button)
        # Здесь необходим time, т.к. сайт тормозит (не успеваем номер заказа передать в переменную)
        time.sleep(5)
        res = self.find_element_located(Locators.new_order_name).text
        # Закрываем модальное окно, чтобы в дальнейшем код возможно было использовать
        close_modal = self.find_element_located(Locators.close_modal)
        ActionChains(self.driver).move_to_element(close_modal).click().perform()
        return res
