from selenium.webdriver.common.by import By
from controls.base_control import BaseControl


class Selector(BaseControl):

    SELECTOR_XPATH = "//button[normalize-space()='{}']"

    def __init__(self, driver, option=None):
        super().__init__(driver)
        if option:
            self._locator = (By.XPATH, self.SELECTOR_XPATH.format(option))
        else:
            self._locator = (By.XPATH, "//div[@class='show dropdown']")
        self.options = (By.XPATH, "//div/a[class='dropdown-item']")
        self.option_value = "//div/a[normalize-space()='{}']"
        self.selected_value = (By.XPATH, "//button[contains(@class,'selected dropdown-toggle')]")
        self.language_option = "//div[contains(@class,'custom-checkbox')]//label[normalize-space()='{}']"

    def select_by_value(self, value):
        """
        Select value by visible text
        :param value: value to be selected from selector
        """
        option = (By.XPATH, self.option_value.format(value))
        element = self._get_web_element()
        element.click()
        element.find_element(*option).click()

    def get_selected_values(self):
        """
        Get selected values from selector
        """
        results = self.driver.find_elements(*self.selected_value)
        return [el.text for el in results]

    def check_value_from_selector(self, value):
        """
        Check value by value
        :param value: value to be checked from selector
        """
        option = (By.XPATH, self.language_option.format(value))
        element = self._get_web_element()
        element.click()
        element.find_element(*option).click()
        element.click()
