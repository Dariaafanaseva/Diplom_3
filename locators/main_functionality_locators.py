from selenium.webdriver.common.by import By

class MainFunctionalityLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]/parent::a'
    ORDER_FEED = By.XPATH, '//a[@href="/feed"]'
    ORDER_FEED_HEADER = By.XPATH, '//h1[contains(text(),"Лента заказов")]'
    CLOSE_DETAILS = By.XPATH, '//button[@type="button"]'
    FLUORESCENT_BUN_NAME = By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]'
    POPUP_WINDOW_HEADER = By.XPATH, '//h2[contains(text(),"Детали ингредиента")]'
    COUNTER_INGREDIENT = By.XPATH, '(//p[@class="counter_counter__num__3nue1"])[1]'
    CONSTRUCTOR_OF_BURGERS = By.XPATH, '//div[@class ="constructor-element constructor-element_pos_top"]'
    CONSTRUCTOR_BURGER_PRICE = By.XPATH, '//p[@class ="text text_type_digits-medium mr-3"]'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "Modal_modal__title_shadow")]'
    WINDOW_WITH_ORDER_NUMBER = By.XPATH, '//*[contains(@class, "Modal_modal__container")]'
