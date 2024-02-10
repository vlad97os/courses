from selenium.webdriver.common.by import By

from pages.base import BasePage

SEARCH_RESULT_TITLES = (By.XPATH, '//a[@class="rf-serp-name-link"]')


class SearchPage(BasePage):

    def get_first_result_header(self) -> str:
        headers = self.find_elements(SEARCH_RESULT_TITLES)
        return headers[0].text
