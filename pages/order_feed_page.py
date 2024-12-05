import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.main_functionality_locators import MainFunctionalityLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.order_feed_locators import OrderFeedLocators
from data import EMAIL, PASSWORD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderFeedPage(BasePage):
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

    @allure.step('Оформление заказа')
    def make_order(self):
        self.find_element_visibility(MainFunctionalityLocators.FLUORESCENT_BUN_NAME)
        self.drag_and_drop_element(MainFunctionalityLocators.FLUORESCENT_BUN_NAME,
                                   MainFunctionalityLocators.CONSTRUCTOR_OF_BURGERS)
        price = self.get_text_from_element(MainFunctionalityLocators.CONSTRUCTOR_BURGER_PRICE)
        if int(price) > 0:
            self.click_element_if_visible(MainPageLocators.MAKE_ORDER_BUTTON)
            self.find_element_visibility(MainFunctionalityLocators.ORDER_NUMBER)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        wait = WebDriverWait(self.driver, 15)
        actual_order_number = wait.until(lambda driver:
            driver.find_element(*MainFunctionalityLocators.ORDER_NUMBER).text if
            driver.find_element(*MainFunctionalityLocators.ORDER_NUMBER).text != "9999" else None
                                         )
        return actual_order_number

    @allure.step('Закрытие всплывающего окна кликом по крестику')
    def close_popup(self):
        self.click_element_if_visible(MainFunctionalityLocators.CLOSE_DETAILS)
        self.waiting_invisibility(OrderFeedLocators.DEFAULT_ORDER_NUMBER)

    @allure.step('Переход в раздел "История заказов"')
    def go_to_orders_history(self):
        self.click_element_if_visible(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        self.click_element_if_visible(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDERS_LIST)


    @allure.step('Переход по клику на "Лента заказов"')
    def click_on_order_feed(self):
        self.find_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        self.click_element_if_visible(MainFunctionalityLocators.ORDER_FEED)
        self.find_element_visibility(MainFunctionalityLocators.ORDER_FEED_HEADER)

    @allure.step('Поиск заказа по номеру в ленте заказов или истории заказов')
    def find_order_by_number(self, order_number):
        xpath_order = f"//*[@class='text text_type_digits-default' and contains(text(), '{order_number}')]"
        order_element = self.driver.find_element(By.XPATH, xpath_order)
        return order_element

    @allure.step('Клик по заказу')
    def click_order(self, order):
        order.click()
        self.find_element_with_wait(OrderFeedLocators.ORDER_NAME_IN_DETAILS)

    @allure.step('Проверка отображения окна с деталями заказа')
    def is_popup_displayed(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderFeedLocators.POPUP_ORDER_DETAILS)
        )
        return self.driver.find_element(*OrderFeedLocators.POPUP_ORDER_DETAILS).is_displayed()

    @allure.step('Извлечение текущего значения счетчика "Выполнено за все время"')
    def current_count_all_time(self):
        current_count_element = self.driver.find_element(*OrderFeedLocators.ALL_TIME_COUNTER)
        current_count_all_time = int(current_count_element.text)
        print(f"Current count all time: {current_count_all_time}")
        return current_count_all_time

    @allure.step('Извлечение текущего значения счетчика "Выполнено за сегодня"')
    def current_count_today(self):
        current_count_element = self.driver.find_element(*OrderFeedLocators.TODAY_COUNTER)
        current_count_today = int(current_count_element.text)
        print(f"Current count today: {current_count_today}")
        return current_count_today

    @allure.step('Ожидание исчезновения надписи "Все текущие заказы готовы!"')
    def waiting_disappearing_orders_are_ready(self):
        self.waiting_invisibility(OrderFeedLocators.ALL_ORDERS_ARE_READY)
        self.find_element_visibility(OrderFeedLocators.CURRENT_ORDER_NUMBER_IN_ORDER_FEED)

    @allure.step('Извление номера заказа в разделе "в работе"')
    def extract_order_number(self):
        self.find_element_visibility(OrderFeedLocators.CURRENT_ORDER_NUMBER_IN_ORDER_FEED)
        order_number_in_order_feed = int(self.get_text_from_element(OrderFeedLocators.CURRENT_ORDER_NUMBER_IN_ORDER_FEED))
        print(f"Order number in order feed: {order_number_in_order_feed}")
        return order_number_in_order_feed









