from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from controls.selector import Selector


class VacancyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.all_departments_selector = Selector(driver=driver, option="All departments")
        self.all_languages_selector = Selector(driver=driver, option="All languages")
        self.all_vacancies = (By.XPATH, "//div[contains(@class, 'flex-column')]//a[contains(@class,'card')]//a")

    def select_option_from_all_departments_selector(self, value):
        self.all_departments_selector.select_by_value(value)

    def get_selected_all_departments_values(self):
        return self.all_departments_selector.get_selected_values()

    def select_language_option(self, value):
        self.all_languages_selector.check_value_from_selector(value)

    def get_number_of_vacancies(self):
        elements = self.driver.find_elements(*self.all_vacancies)
        return len(elements)
