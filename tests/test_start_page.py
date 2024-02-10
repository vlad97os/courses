from pages.detailed_information_entertainment import DetailedInformationEntertainmentPage
from pages.entertainment import EntertainmentPage


def test_links_general_directory(start_page, browser):
    title_apple_books = 'Apple Books'
    start_page.open_apple_books()
    detailed_information_entertainment_page = DetailedInformationEntertainmentPage(browser)
    assert detailed_information_entertainment_page.get_title() == title_apple_books


def test_links_in_footer(start_page):
    footer_links = ['Privacy Policy', 'Terms of Use', 'Sales and Refunds', 'Legal', 'Site Map']
    assert start_page.get_links_in_footer() == footer_links


def test_links_in_header(start_page):
    header_links = ['Apple', 'Store', 'Mac', 'iPad', 'iPhone', 'Watch', 'Vision', 'AirPods',
                    'TV & Home', 'Entertainment', 'Accessories', 'Support']
    assert start_page.get_links_in_header() == header_links


def test_bread_crumbs(start_page, browser):
    second_bread_crumb = 'Entertainment'
    third_bread_crumb = 'Apple Podcasts'
    title_start_page = 'Apple'
    start_page.open_apple_podcasts()
    detailed_information_entertainment_page = DetailedInformationEntertainmentPage(browser)
    assert detailed_information_entertainment_page.get_second_bread_crumb() == second_bread_crumb
    assert detailed_information_entertainment_page.get_third_bread_crumb() == third_bread_crumb
    detailed_information_entertainment_page.transition_by_bread_crumbs()
    entertainment_page = EntertainmentPage(browser)
    assert entertainment_page.get_second_bread_crumb() == second_bread_crumb
    entertainment_page.transition_by_bread_crumbs()
    assert browser.title == title_start_page
