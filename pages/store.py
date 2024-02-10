from selenium.webdriver.common.by import By

from pages.base import BasePage

AIRPODS = (By.XPATH, '//a[@href="https://www.apple.com/airpods"]')


class StorePage(BasePage):
    def open_product_group(self):
        self.click_element(AIRPODS)
