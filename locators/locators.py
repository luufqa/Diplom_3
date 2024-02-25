from selenium.webdriver.common.by import By

class Urls:
    # base url
    base_url = 'https://stellarburgers.nomoreparties.site/'
class Account:
    # test account
    first_user_email = 'luufqa@gmail.com'
    first_user_password = '3607833465'
    second_user_email = 'unkpleasure@gmail.com'
    second_user_password = '3607833466'

class Headers:
    # headers group
    constructor = (By.LINK_TEXT, 'Конструктор')
    feed = (By.XPATH, './/a[@href="/feed"]')
    login_button = (By.XPATH, './/a[@href="/account"]')

class Restore:
    # restore group
    restore_button = (By.XPATH, './/a[@href="/forgot-password"]')
    restore_input_email = (By.XPATH, './/input[@class="text input__textfield text_type_main-default"]')
    accept_restore_button = (By.XPATH, './/*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                                       'button_button_size_medium__3zxIa"]')
    visible_password = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    change_active_field = (By.XPATH, './/*[@class="input pr-6 pl-6 input_type_text input_size_default '
                                     'input_status_active"]')
class Auth:
    # auth group
    login_field = (By.XPATH, './/input[@type="text"]')
    password_field = (By.XPATH, './/input[@type="password"]')
    accept_login_button = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                                     'button_button_size_medium__3zxIa"]')
    history_button = (By.XPATH, './/*[@href="/account/order-history"]')
    history_number_order = (By.XPATH, './/p[@class="text text_type_digits-default"]')
    history_today_order = (By.XPATH, './/p[@class="text text_type_main-default text_color_inactive"]')
    logout_button = (By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium '
                               'text_color_inactive"]')
class Constructor:
    # constructor menu
    first_ingredient = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_')][1]")
    close_modal = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    field_for_order = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    accept_order_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                     "button_button_size_large__G21Vg']")
    new_order_name = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text '
                                'text_type_digits-large mb-8"]')
class Feed:

    # feed menu
    counter_for_all_time = (By.XPATH, './/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    counter_for_today = (By.XPATH, './/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    order_in_progress = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')
