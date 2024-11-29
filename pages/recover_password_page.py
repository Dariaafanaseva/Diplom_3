import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.recover_password_locators import RecoverPageLocators
from data import EMAIL


class RecoverPasswordPage(BasePage):
    @allure.step('Переход на страницу бургеров')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def go_to_page_recover_password(self):
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(RecoverPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_to_element(RecoverPageLocators.RECOVER_PASSWORD_BUTTON)
        self.add_text_to_element(RecoverPageLocators.RECOVER_PASSWORD_INPUT, EMAIL)
        self.click_to_element(RecoverPageLocators.RECOVER_BUTTON)
        self.find_element_visibility(RecoverPageLocators.SAVE_BUTTON)

    @allure.step('Клик по кнопке показать/скрыть пароль ')
    def click_to_show_password(self):
        self.find_element_with_wait(RecoverPageLocators.EYE_ICON).click

    @allure.step('Проверка активности поля пароль')
    def is_password_input_enable(self):
        get_password_input = self.find_element_visibility(RecoverPageLocators.PASSWORD_INPUT)
        return get_password_input.is_enabled()




