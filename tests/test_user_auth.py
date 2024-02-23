import allure
from pages.base_page import BasePage
from pages.user_auth import UserAuth


class TestUserAuth:

    @allure.title('Проверка Личного кабинета')
    def test_restore(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        user_auth.check_history_list()
        assert base_page.current_url() == "https://stellarburgers.nomoreparties.site/login"
