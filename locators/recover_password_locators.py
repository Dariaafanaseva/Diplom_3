from selenium.webdriver.common.by import By

class RecoverPageLocators:

    RECOVER_PASSWORD_BUTTON= By.XPATH, '//a[contains(text(),"Восстановить пароль")]'
    RECOVER_PASSWORD_INPUT = By.XPATH, '//input[@name="name"]'
    RECOVER_BUTTON = By.XPATH, '//button[contains(text(),"Восстановить")]'
    RECOVER_PASSWORD_HEADER = By.XPATH, '//h2[contains(text(),"Восстановление пароля")]'
    SAVE_BUTTON = By.XPATH, '//button[contains(text(),"Сохранить")]'
    EYE_ICON = By.XPATH, '//div[@class ="input__icon input__icon-action"]//*[name()="svg"]'
    PASSWORD_INPUT = By.XPATH, '//input[@name="Введите новый пароль"]'
    BLUE_FRAME_PASSWORD_FIELD = By.XPATH, '//div[@class ="input pr-6 lp-6 input_type_text_input_size_default_input_status_active"]'
