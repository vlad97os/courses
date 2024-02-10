from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from pages.start import StartPage
from pages.support import SupportPage
from config.logger import log

START_URL = 'https://www.apple.com/'


@pytest.fixture(scope='session')
def browser() -> webdriver:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1024,600')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(0.5)
    log.info('browser started')
    yield chrome_browser
    chrome_browser.quit()
    log.info('browser closed')


@pytest.fixture(scope='function', autouse=True)
def open_start_page(browser):
    browser.get(START_URL)


@pytest.fixture(scope='session')
def start_page(browser):
    start_page = StartPage(browser)
    return start_page


@pytest.fixture(scope='session')
def support_page(browser):
    support_page = SupportPage(browser)
    return support_page


@pytest.fixture(scope='function')
def search_on_support_page(start_page, support_page):
    start_page.open_support()
    support_page.open_search()
    return support_page
