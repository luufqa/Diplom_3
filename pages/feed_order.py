from selenium.webdriver import ActionChains
from locators.locators import Locators
from pages.base_page import BasePage
import allure
import time


class FeedOrders(BasePage):
    @allure.step('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def user_order_in_feed_orders(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        self.find_element_located_click(Locators.history_button)

        # Добавляем в список заказы пользователя за Сегодня
        history_number = self.find_element_all_located(Locators.history_number_order)
        order_names = [order.text for order in history_number]
        history_today = self.find_element_all_located(Locators.history_today_order)
        order_today = [order.text for order in history_today]
        user_orders = []
        for i, g in zip(order_names, order_today):
            if 'Сегодня' in g:
                user_orders.append(i)

        # Добавляем в список заказы, которые находятся в общей ленте заказов
        skip_modal_and_go_feed = self.find_element_located(Locators.feed)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_feed).click().perform()
        order_names_list = self.find_element_all_located(Locators.history_number_order)
        all_orders = [order.text for order in order_names_list]

        # Возвращаем два списка, чтобы сравнить
        return user_orders, all_orders

    @allure.step('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def counter_for_all_time(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        skip_modal_and_go_feed = self.find_element_located(Locators.feed)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_feed).click().perform()
        counter_for_all_time = self.find_element_located(Locators.counter_for_all_time).text
        return counter_for_all_time

    @allure.step('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def counter_for_today(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        skip_modal_and_go_feed = self.find_element_located(Locators.feed)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_feed).click().perform()
        counter_for_today = self.find_element_located(Locators.counter_for_today).text
        return counter_for_today

    @allure.step('После оформления заказа его номер появляется в разделе В работе')
    def order_in_progress(self):
        skip_modal_and_go_login = self.find_element_located(Locators.login_button)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_login).click().perform()
        skip_modal_and_go_feed = self.find_element_located(Locators.feed)
        ActionChains(self.driver).move_to_element(skip_modal_and_go_feed).click().perform()
        # Здесь необходим time, т.к. сайт тормозит (не успеваем номер заказа передать в переменную)
        time.sleep(9)
        order_in_progress = self.find_element_located(Locators.order_in_progress).text
        return order_in_progress
