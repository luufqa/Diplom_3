import allure
from pages.base_page import BasePage
from pages.main_function import MainFunction
from pages.user_auth import UserAuth


class TestMainFunction:

    @allure.title('Проверка основного функционала')
    def test_main_function(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        main_function = MainFunction(driver)
        user_auth = UserAuth(driver)
        user_auth.user_auth()
        res = main_function.main_function()
        assert len(res) == 5
