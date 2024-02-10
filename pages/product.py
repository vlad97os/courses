from selenium.webdriver.common.by import By

from pages.base import BasePage

BUTTON_ADD_TO_BAG = (By.ID, 'add-to-cart')
TITLE_AIRPODS_PRO = (By.XPATH, '//h1[@data-autom="productTitle"]')
FULL_PRICE_AIRPODS_PRO = (By.XPATH, '//span[@class="rc-prices-fullprice"]')


class ProductPage(BasePage):
    def add_to_bag(self):
        self.click_element(BUTTON_ADD_TO_BAG)

    def get_product_title(self) -> str:
        return self.find_element(TITLE_AIRPODS_PRO).text

    def get_full_product_price(self) -> str:
        return self.find_element(FULL_PRICE_AIRPODS_PRO).text
