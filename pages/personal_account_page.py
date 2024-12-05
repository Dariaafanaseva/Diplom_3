import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from data import EMAIL, PASSWORD

class PersonalAccountPage(BasePage):
    @allure.step('Переход на страницу бургеров')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Авторизация по клику на "Личный кабинет"')
    def login_personal_account(self):
        self.find_element_with_wait(MainPageLocators.ACCOUNT_BUTTON)
        self.click_element_if_visible(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(MainPageLocators.LOGIN_HEADER)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_EMAIL_INPUT_FIELD, EMAIL)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_PASSWORD_INPUT_FIELD, PASSWORD)
        self.click_element_if_visible(PersonalAccountLocators.LOGIN_APPLY_BUTTON)
        self.find_element_visibility(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Переход в раздел "История заказов"')
    def go_to_orders_history(self):
        self.click_element_if_visible(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        self.click_element_if_visible(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDERS_LIST)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click_element_if_visible(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        self.click_element_if_visible(PersonalAccountLocators.LOGOUT_BUTTON)
        self.find_element_visibility(MainPageLocators.LOGIN_HEADER)




