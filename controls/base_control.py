from selenium.webdriver import ActionChains


class BaseControl:
    """
    Represents base class UI controls
    :param driver: instance of WebDriver

    """
    def __init__(self, driver):
        self.driver = driver
        self.__locator = None

    @property
    def _locator(self):
        """Returns Control locator"""
        return self.__locator

    @_locator.setter
    def _locator(self, locator):
        """
        Set Control locator
        :param locator: tuple (By.<CSS/XPATH/etc>, 'locator')
        """
        if not isinstance(locator, tuple):
            raise ValueError("Locator must be a tuple (By.<CSS/XPATH/etc>, 'locator')")
        self.__locator = locator

    def _get_web_element(self):
        """
        Waits for a parent and gets WebElement of locator
        :return: WebElement of _locator
        """
        return self.driver.find_element(*self._locator)

    def click(self):
        """
        Waits for element becomes clickable and performs click
        """
        element = self._get_web_element()
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        return element.click()

    def find_element_execute_script(self):
        """
        Toggle checkbox independently of the status
        """
        element = self._get_web_element()
        self.driver.execute_script("arguments[0].click();", element)
