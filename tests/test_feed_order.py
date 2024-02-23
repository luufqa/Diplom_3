import allure
from pages.base_page import BasePage
from pages.main_function import MainFunction
from pages.feed_order import FeedOrders
from pages.user_auth import UserAuth


class TestFeedOrders:

    @allure.title('Проверка раздела "Лента заказов"')
    def test_user_order_in_feed_orders(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        feed_order = FeedOrders(driver)
        user_orders, all_orders = feed_order.user_order_in_feed_orders()
        assert user_orders[-1] in all_orders

    @allure.title('Проверка счетчика заказов "Выполнено за всё время"')
    def test_counter_for_all_time(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        feed_order = FeedOrders(driver)
        old_result = feed_order.counter_for_all_time()
        main_function = MainFunction(driver)
        main_function.main_function()
        new_result = feed_order.counter_for_all_time()
        assert old_result != new_result

    @allure.title('Проверка счетчика заказов "Выполнено за сегодня"')
    def test_counter_for_today(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        feed_order = FeedOrders(driver)
        old_result = feed_order.counter_for_today()
        main_function = MainFunction(driver)
        main_function.main_function()
        new_result = feed_order.counter_for_today()
        assert old_result != new_result

    @allure.title('Проверка номера заказа, появляется в разделе "В работе"')
    def test_order_in_progress(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        feed_order = FeedOrders(driver)
        main_function = MainFunction(driver)
        new_order = main_function.main_function()
        order_in_progress = feed_order.order_in_progress()
        assert new_order in order_in_progress
