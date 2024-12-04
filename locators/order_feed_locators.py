from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_IN_ORDER_FEED = By.XPATH, '//ul[contains(@class,"OrderFeed_list")]/li[1]'
    POPUP_ORDER_DETAILS = By.XPATH, '//div[contains(@class, "Modal_orderBox")]'
    ORDER_NAME_IN_DETAILS = By.XPATH, '//h2[contains(@class, "text text_type_main-medium")]'
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[contains(text(),"09999")]'
    ALL_TIME_COUNTER = By.XPATH, '//div[p[text()="Выполнено за все время:"]]/p[2]'
    TODAY_COUNTER = By.XPATH, '//div[p[text()="Выполнено за сегодня:"]]/p[2]'