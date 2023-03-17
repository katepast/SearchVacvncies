import pytest
from selenium import webdriver
from helpers.web_driver.practice_web_driver import WebDriver, WebDriverListener
from project_const import chromedriver_path
from Pages.vacancy_page import VacancyPage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver = WebDriver(driver, WebDriverListener())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_vacancy_site(browser):
    base_page = VacancyPage(browser)
    base_page.open_url()
    yield browser









