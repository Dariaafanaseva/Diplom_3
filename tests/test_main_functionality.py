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

    @allure.description(
        'Появление всплывающего окна с деталями, если кликнуть на ингредиент')
    def test_click_on_ingredient(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.click_on_ingredient()
        assert main_functionality.is_popup_displayed() is True

    @allure.description(
        'Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_popup(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.click_on_ingredient()
        main_functionality.close_popup()
        popup_not_visible = not main_functionality.is_popup_displayed()
        assert popup_not_visible is True

    @allure.description(
        'Проверка возможности оформления заказа у залогиненного пользователя')
    def test_make_order_authorised(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.login_personal_account()
        main_functionality.add_ingredient()
        window_with_order_number = main_functionality.make_order()
        assert window_with_order_number is True

    @allure.description(
        'Проверка увеличения каунтера при добавлении ингредиента')
    def test_increase_of_ingredient_counter(self, driver):
        main_functionality = MainFunctionalityPage(driver)
        main_functionality.get(BASE_URL)
        main_functionality.login_personal_account()
        initial_count = main_functionality.current_count()
        print(f"Initial count: {initial_count}")
        main_functionality.add_ingredient()
        new_count_value = main_functionality.new_count()
        print(f"New count after adding ingredient: {new_count_value}")
        assert new_count_value > initial_count


