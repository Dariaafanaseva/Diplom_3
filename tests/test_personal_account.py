from pages.personal_account_page import PersonalAccountPage
import allure
from data import BASE_URL, ORDERS_HISTORY, LOGIN_URL

class TestPersonalAccount:
    @allure.description(
        'Проверка перехода по клику на "Личный кабинет"')
    def test_go_to_page_recover_password(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.get(BASE_URL)
        personal_account.login_personal_account()
        assert driver.current_url == BASE_URL

    @allure.description(
        'Проверка перехода в раздел "История заказов"')
    def test_go_to_page_recover_password(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.get(BASE_URL)
        personal_account.login_personal_account()
        personal_account.go_to_orders_history()
        assert driver.current_url == ORDERS_HISTORY

    @allure.description(
        'Проверка выхода из аккаунта')
    def test_logout_from_account(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.get(BASE_URL)
        personal_account.login_personal_account()
        personal_account.logout()
        assert driver.current_url == LOGIN_URL
