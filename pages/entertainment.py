from selenium.webdriver.common.by import By

from pages.base import BasePage
FIRST_BREAD_CRUMB = (By.XPATH, '//a[@class="home ac-gf-breadcrumbs-home"]')
SECOND_BREAD_CRUMB = (By.XPATH, '//li[@class="ac-gf-breadcrumbs-item"]/span')


class EntertainmentPage(BasePage):

    def get_second_bread_crumb(self) -> str:
        return self.find_element(SECOND_BREAD_CRUMB).text

    def transition_by_bread_crumbs(self):
        self.click_element(FIRST_BREAD_CRUMB)
