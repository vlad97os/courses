from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

waiting_time = 90


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.browser, waiting_time).until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return WebDriverWait(self.browser, waiting_time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple[str, str]):
        WebDriverWait(self.browser, waiting_time).until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator: tuple[str, str], text: str):
        WebDriverWait(self.browser, waiting_time).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def click_keyboard(self, locator: tuple[str, str]):
        WebDriverWait(self.browser, waiting_time).until(EC.element_to_be_clickable(locator)).send_keys(Keys.ENTER)
