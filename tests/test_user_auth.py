import allure
from pages.user_auth import UserAuth
from locators.locators import Urls
from locators.locators import Account
import pytest


class TestUserAuth:
    @pytest.mark.parametrize('user_login, user_password', [(Account.first_user_email, Account.first_user_password),
                                                           (Account.second_user_email, Account.second_user_password)])
    @allure.title('Проверка Личного кабинета')
    def test_restore(self, driver, user_login, user_password):
        user_auth = UserAuth(driver)
        user_auth.go_to_site(Urls.base_url)
        user_auth.user_auth(user_login, user_password)
        user_auth.check_history_list()
        assert user_auth.current_url() == "https://stellarburgers.nomoreparties.site/login"
