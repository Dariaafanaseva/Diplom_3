from pages.order_feed_page import OrderFeedPage
import allure
from data import BASE_URL

class TestOrderFeed:
    @allure.description(
        'Проверка появления окна с деталями, при клике на заказ')
    def test_click_on_order(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.get(BASE_URL)
        order_feed.login_personal_account()
        order_feed.make_order()
        actual_order_number = order_feed.get_order_number()
        print(f"Актуальный номер заказа: {actual_order_number}")
        order_feed.close_popup()
        order_feed.click_on_order_feed()
        order = order_feed.find_order_by_number(actual_order_number)
        order_feed.click_order(order)
        assert order_feed.is_popup_displayed() is True

    @allure.description(
        'Проверка появления заказа из истории заказов в ленте заказов')
    def test_order_appearance_on_order_feed(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.get(BASE_URL)
        order_feed.login_personal_account()
        order_feed.make_order()
        actual_order_number = order_feed.get_order_number()
        order_feed.close_popup()
        order_feed.go_to_orders_history()
        order_number_in_order_history = (order_feed.find_order_by_number(actual_order_number)).text
        order_feed.click_on_order_feed()
        order_number_in_order_feed = (order_feed.find_order_by_number(actual_order_number)).text
        assert order_number_in_order_history == order_number_in_order_feed

    @allure.description(
        'Проверка увеличения счетчика "Выполнено за все время" при оформлении заказа')
    def test_increase_all_time_counter(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.get(BASE_URL)
        order_feed.login_personal_account()
        order_feed.click_on_order_feed()
        count_before_order = order_feed.current_count_all_time()
        order_feed.get(BASE_URL)
        order_feed.make_order()
        order_feed.close_popup()
        order_feed.click_on_order_feed()
        count_after_order = order_feed.current_count_all_time()
        assert count_after_order > count_before_order

    @allure.description(
        'Проверка увеличения счетчика "Выполнено за сегодня" при оформлении заказа')
    def test_increase_today_counter(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.get(BASE_URL)
        order_feed.login_personal_account()
        order_feed.click_on_order_feed()
        count_before_order = order_feed.current_count_today()
        print(count_before_order)
        order_feed.get(BASE_URL)
        order_feed.make_order()
        order_feed.close_popup()
        order_feed.click_on_order_feed()
        count_after_order = order_feed.current_count_today()
        print(count_after_order)
        assert count_after_order > count_before_order

    @allure.description(
        'Проверка появления номера заказа в разделе "в работе"')
    def test_increase_today_counter(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.get(BASE_URL)
        order_feed.login_personal_account()
        order_feed.make_order()
        actual_order_number = int(order_feed.get_order_number())
        print(actual_order_number)
        order_feed.close_popup()
        order_feed.click_on_order_feed()
        order_feed.waiting_disappearing_orders_are_ready()
        order_number_in_order_feed = order_feed.extract_order_number()
        print(order_number_in_order_feed)
        assert actual_order_number == order_number_in_order_feed





