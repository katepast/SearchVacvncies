from configs.config import BASE_URL
from conftest import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url: str = BASE_URL):
        self.driver.get(url)
