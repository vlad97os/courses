from selenium.webdriver.common.by import By

from pages.base import BasePage

SEARCH_FIELD = (By.XPATH, '//input[@aria-owns="as-search-suggestions"]')
SEARCH_RESULTS = (By.XPATH, '//li[@class="as-search-suggestion"]')
FIRST_QUICK_LINK = (By.XPATH, '//li[@id="as-search-quicklinks-0"]/a')


class SupportPage(BasePage):
    def input_in_search(self, text: str):
        self.input_text(SEARCH_FIELD, text)

    def open_search(self):
        self.click_element(SEARCH_FIELD)

    def get_number_of_search_results(self) -> int:
        return len(self.find_elements(SEARCH_RESULTS))

    def click_first_quick_link(self):
        self.click_element(FIRST_QUICK_LINK)

    def get_text_first_quick_link(self) -> str:
        return self.find_element(FIRST_QUICK_LINK).text
