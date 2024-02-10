from selenium.webdriver.common.by import By

from pages.base import BasePage

REGION_MAROC = (By.XPATH, "//span[contains(text(), 'Maroc')]")


class ChooseRegionPage(BasePage):

    def click_region(self):
        self.click_element(REGION_MAROC)

