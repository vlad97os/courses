from selenium.webdriver.common.by import By

from pages.base import BasePage

BUTTON_REMOVE_PRODUCT = (By.XPATH, '//button[@class="rs-iteminfo-remove as-buttonlink"]')
TITLE_AIRPODS_PRO = (By.XPATH, '//a[@data-autom="bag-item-name"]')
FULL_PRICE_AIRPODS_PRO = (By.XPATH, '//div[@data-autom="Monthly_price"]')


class BagPage(BasePage):
    def get_product_title(self) -> str:
        return self.find_element(TITLE_AIRPODS_PRO).text

    def get_full_product_price(self) -> str:
        return self.find_element(FULL_PRICE_AIRPODS_PRO).text

    def remove_product(self):
        self.click_element(BUTTON_REMOVE_PRODUCT)
