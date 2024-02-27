import allure
import pytest
from pages.main_function import MainFunction
from pages.user_auth import UserAuth
from locators.locators import Urls
from locators.locators import Account


class TestMainFunction:
    @pytest.mark.parametrize('user_login, user_password', [(Account.first_user_email, Account.first_user_password),
                                                           (Account.second_user_email, Account.second_user_password)])
    @allure.title('Проверка основного функционала')
    def test_main_function(self, driver, user_login, user_password):
        main_function = MainFunction(driver)
        user_auth = UserAuth(driver)
        user_auth.go_to_site(Urls.base_url)
        user_auth.user_auth(user_login, user_password)
        res = main_function.main_function()
        assert len(res) == 5
