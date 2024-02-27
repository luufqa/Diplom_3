import allure
from pages.restore_password import RestorePassword
from locators.locators import Urls
from locators.locators import Account


class TestRestorePassword:

    @allure.title('Проверка восстановления пароля')
    def test_restore_password(self, driver):
        restore = RestorePassword(driver)
        restore.go_to_site(Urls.base_url)
        result = restore.restore_password(Account.first_user_email)
        assert 'input_status_active' in result
