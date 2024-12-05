import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.main_functionality_locators import MainFunctionalityLocators
from locators.personal_account_locators import PersonalAccountLocators
from data import EMAIL, PASSWORD

class MainFunctionalityPage(BasePage):
    @allure.step('Переход на страницу бургеров')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Переход по клику на "Конструктор"')
    def click_on_constructor(self):
        self.find_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_visibility(MainPageLocators.LOGIN_HEADER)
        self.click_to_element(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)
        self.find_element_visibility(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Переход по клику на "Лента заказов"')
    def click_on_order_feed(self):
        self.find_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        self.click_to_element(MainFunctionalityLocators.ORDER_FEED)
        self.find_element_visibility(MainFunctionalityLocators.ORDER_FEED_HEADER)

    @allure.step('Переход по клику на ингредиент')
    def click_on_ingredient(self):
        self.find_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        self.move_to_element_and_click(MainFunctionalityLocators.FLUORESCENT_BUN_NAME)
        self.find_element_with_wait(MainFunctionalityLocators.POPUP_WINDOW_HEADER)

    @allure.step('Проверка отображения окна с деталями ингредиента')
    def is_popup_displayed(self):
        return self.driver.find_element(*MainFunctionalityLocators.POPUP_WINDOW_HEADER).is_displayed()


    @allure.step('Закрытие всплывающего окна кликом по крестику')
    def close_popup(self):
        self.click_to_element(MainFunctionalityLocators.CLOSE_DETAILS)
        self.waiting_invisibility(MainFunctionalityLocators.POPUP_WINDOW_HEADER)


    @allure.step('Авторизация по клику на "Личный кабинет"')
    def login_personal_account(self):
        self.click_element_if_visible(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(MainPageLocators.LOGIN_HEADER)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_EMAIL_INPUT_FIELD, EMAIL)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_PASSWORD_INPUT_FIELD, PASSWORD)
        self.click_element_if_visible(PersonalAccountLocators.LOGIN_APPLY_BUTTON)
        self.find_element_visibility(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Извлечение текущего значения каунтера')
    def current_count(self):
        current_count_element = self.driver.find_element(*MainFunctionalityLocators.COUNTER_INGREDIENT)
        current_count = int(current_count_element.text)
        return current_count

    @allure.step('Извлечение нового значения каунтера')
    def new_count(self):
        new_count_element = self.driver.find_element(*MainFunctionalityLocators.COUNTER_INGREDIENT)
        new_count = int(new_count_element.text)
        return new_count


    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        self.find_element_visibility(MainFunctionalityLocators.FLUORESCENT_BUN_NAME)
        self.drag_and_drop_element(MainFunctionalityLocators.FLUORESCENT_BUN_NAME, MainFunctionalityLocators.CONSTRUCTOR_OF_BURGERS)

    @allure.step('Оформление заказа')
    def make_order(self):
        price = self.get_text_from_element(MainFunctionalityLocators.CONSTRUCTOR_BURGER_PRICE)
        if int(price) > 0:
            self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON)
            window_with_order_number = self.find_element_visibility(MainFunctionalityLocators.ORDER_NUMBER)
            return window_with_order_number.is_displayed()

