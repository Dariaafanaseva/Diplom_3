from selenium.webdriver.common.by import By

class MainFunctionalityLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]/parent::a'
    ORDER_FEED = By.XPATH, '//a[@href="/feed"]'
    ORDER_FEED_HEADER = By.XPATH, '//h1[contains(text(),"Лента заказов")]'
