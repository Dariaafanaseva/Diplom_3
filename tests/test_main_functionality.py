from pages.main_functionality_page import MainFunctionalityPage
import allure
from data import BASE_URL, ORDER_FEED_URL

class TestPersonalAccount:
    @allure.description(
        'Проверка перехода по клику на "Конструктор"')
    def test_click_on_constructor(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.click_on_constructor()
        assert driver.current_url == BASE_URL

    @allure.description(
        'Проверка перехода по клику на "Лента заказов"')
    def test_click_on_order_feed(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.click_on_order_feed()
        assert driver.current_url == ORDER_FEED_URL