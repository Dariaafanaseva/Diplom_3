import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.main_functionality_locators import MainFunctionalityLocators

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
