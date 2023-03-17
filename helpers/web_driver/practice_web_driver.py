from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        return WebDriverWait(driver, 4).until(EC.visibility_of_element_located((by, value)))


class WebDriver(EventFiringWebDriver):

    def wait_till_element_is_displayed(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_till_text_present(self, locator, text, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False
