import allure
from pages.base_page import BasePage
from pages.restore_password import RestorePassword


class TestRestorePassword:

    @allure.title('Проверка восстановления пароля')
    def test_restore_password(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://stellarburgers.nomoreparties.site/')
        restore = RestorePassword(driver)
        result = restore.restore_password()
        assert 'input_status_active' in result
