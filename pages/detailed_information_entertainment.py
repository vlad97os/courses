from selenium.webdriver.common.by import By

from pages.base import BasePage

TITLE = (By.XPATH, '//h1[@class="typography-hero-eyebrow"]')
SECOND_BREAD_CRUMB = (By.XPATH, '//a[@class="ac-gf-breadcrumbs-link"]/span')
THIRD_BREAD_CRUMB = (By.XPATH, '//li[@class="ac-gf-breadcrumbs-item"][2]/span')


class DetailedInformationEntertainmentPage(BasePage):

    def get_title(self) -> str:
        return self.find_element(TITLE).text

    def get_second_bread_crumb(self) -> str:
        return self.find_element(SECOND_BREAD_CRUMB).text

    def get_third_bread_crumb(self) -> str:
        return self.find_element(THIRD_BREAD_CRUMB).text

    def transition_by_bread_crumbs(self):
        self.click_element(SECOND_BREAD_CRUMB)
