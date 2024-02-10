from selenium.webdriver.common.by import By

from pages.base import BasePage

TITLE = (By.XPATH, '//h1[@id="howto-title"]')


class DetailedInformationSupportPage(BasePage):
    def get_title(self) -> str:
        return self.find_element(TITLE).text
