from selenium.webdriver.common.by import By

class MainPageLocators:
    # кнопка "личный кабинет" на главной странице:
    ACCOUNT_BUTTON = By.XPATH, '//p[contains(text(),"Личный Кабинет")]'
    LOGIN_HEADER = By.XPATH, '//h2[contains(text(),"Вход")]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти в аккаунт")]'
    MAKE_ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'

