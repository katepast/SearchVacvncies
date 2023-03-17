import pytest
from Pages.vacancy_page import VacancyPage
from helpers.logging import logger


class TestVacancySearch:

    searched_criteria = [("Research & Development", "English", 11)]
    @pytest.mark.debug
    @pytest.mark.parametrize("department,course,vacancy_number", searched_criteria)
    def test_search_vacancy(self, department, course, vacancy_number, open_vacancy_site):
        searched_criteria = ["Research & Development", "English", 11]
        main_page = VacancyPage(open_vacancy_site)

        logger.info(f"Select vacancy department with name '{searched_criteria[0]}'")
        main_page.select_option_from_all_departments_selector(searched_criteria[0])

        logger.info(f"Select language with name '{searched_criteria[1]}'")
        main_page.select_language_option(searched_criteria[1])

        logger.info(f"Verify that selected vacancies '{department, course} is displayed in the drop down")
        assert [department, course] == main_page.get_selected_all_departments_values()

        logger.info(f"Verify the number of founded vacancies equal to '{vacancy_number}'")
        assert vacancy_number == main_page.get_number_of_vacancies()
