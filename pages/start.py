from selenium.webdriver.common.by import By

from pages.base import BasePage

SEARCH_BUTTON = (By.XPATH, '//a[@id="globalnav-menubutton-link-search"]')
SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Search apple.com"]')
STORE_BUTTON = (By.XPATH, '//div[@data-analytics-element-engagement="globalnav hover - store"]')
SUPPORT_BUTTON = (By.XPATH, '//div[@data-analytics-element-engagement="globalnav hover - support"]')
DROPDOWN = (By.ID, 'ac-ls-dropdown')
CURRENT_REGION = (By.XPATH, '//div[@id="ac-ls-dropdown-select"]//span[@class="ac-ls-dropdown-copy"]')
FOOTER_LINKS = (By.XPATH, '//a[@class="ac-gf-footer-legal-link"]')
HEADER_LINKS = (By.XPATH, '//span[@class="globalnav-link-text"]')
OTHER_COUNTRY = (By.XPATH, '//li[@id="ac-ls-dropdown-option-country-region"]//span[@class="ac-ls-dropdown-copy"]')
CONTINUE_BUTTON = (By.ID, 'ac-ls-continue')
APPLE_BOOKS_LINK = (By.XPATH, '//li[@class="ac-gf-directory-column-section-item"]/a[@data-analytics-title="apple '
                              'books"]')
APPLE_PODCAST_LINK = (By.XPATH, '//li[@class="ac-gf-directory-column-section-item"]/a[@data-analytics-title="apple '
                                'podcasts"]')


class StartPage(BasePage):

    def open_search(self):
        self.click_element(SEARCH_BUTTON)

    def input_in_search(self, text: str):
        self.input_text(SEARCH_FIELD, text)

    def click_enter(self):
        self.click_keyboard(SEARCH_FIELD)

    def open_store(self):
        self.click_element(STORE_BUTTON)

    def open_support(self):
        self.click_element(SUPPORT_BUTTON)

    def open_dropdown(self):
        self.click_element(DROPDOWN)

    def click_other_country(self):
        self.click_element(OTHER_COUNTRY)

    def click_continue(self):
        self.click_element(CONTINUE_BUTTON)

    def get_current_region(self) -> str:
        return self.find_element(CURRENT_REGION).text

    def get_links_in_footer(self) -> list[str]:
        links = self.find_elements(FOOTER_LINKS)
        text_links = [link.text for link in links]
        return text_links

    def open_apple_books(self):
        self.click_element(APPLE_BOOKS_LINK)

    def open_apple_podcasts(self):
        self.click_element(APPLE_PODCAST_LINK)

    def get_links_in_header(self) -> list[str]:
        links = self.find_elements(HEADER_LINKS)
        text_links = [link.text for link in links]
        return text_links
