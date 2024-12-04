from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    # def click_on_element_js(self, locator):
    #     self.driver.execute_script("arguments[0].click();", locator)

    # WebDriverWait(self.driver, self.timeout).until(
    #     lambda driver: get_text_from_element(locator))

    def click_element_if_visible(self, locator):
        element = self.find_element_visibility(locator)
        self.driver.execute_script('arguments[0].click();', element)

    def waiting_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element(locator)
        )

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def find_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
            locator))

    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

    def drag_and_drop_element(self, locator_from, locator_to):
        self.find_element_visibility(locator_from)
        self.find_element_visibility(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)

        self.driver.execute_script("""
                       var source = arguments[0];
                       var target = arguments[1];
                       var evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
    evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                   """, element_from, element_to)



