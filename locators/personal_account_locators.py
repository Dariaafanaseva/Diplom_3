from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    LOGIN_EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')
    LOGIN_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    LOGIN_APPLY_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    ORDERS_HISTORY_BUTTON = By.XPATH, '//a[contains(text(),"История заказов")]'
    ORDERS_LIST = By.XPATH, '//*[contains(@class, "OrderHistory_profileList")]'
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')