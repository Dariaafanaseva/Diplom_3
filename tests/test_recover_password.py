from pages.recover_password_page import RecoverPasswordPage
import allure
from data import BASE_URL, RESET_PASSWORD_URL

class TestRecoverPassword:
    @allure.description(
        'Проверка перехода по кнопке "Восстановить пароль", ввода почты и клик по кнопке «Восстановить»')
    def test_go_to_page_recover_password(self, driver):
        recover_password = RecoverPasswordPage(driver)
        recover_password.get(BASE_URL)
        recover_password.go_to_page_recover_password()
        assert driver.current_url == RESET_PASSWORD_URL

    @allure.description(
        'Проверка клика по кнопке показать/скрыть пароль делает поле активным')
    def test_click_to_eye(self, driver):
        recover_password = RecoverPasswordPage(driver)
        recover_password.get(BASE_URL)
        recover_password.go_to_page_recover_password()
        assert recover_password.is_password_input_enable() is True



