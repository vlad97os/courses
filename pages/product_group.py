from selenium.webdriver.common.by import By

from pages.base import BasePage

BUTTON_BUY_AIRPODS_PRO = (By.XPATH, '//a[@data-analytics-title="buy - airpods pro (2nd generation)"]')


class ProductGroupPage(BasePage):
    def open_product(self):
        self.click_element(BUTTON_BUY_AIRPODS_PRO)
