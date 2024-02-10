from pages.search import SearchPage


def test_general_search(browser, start_page):
    search_request = 'iPhone 15'
    start_page.open_search()
    start_page.input_in_search(search_request)
    start_page.click_enter()
    search_page = SearchPage(browser)
    assert search_request in search_page.get_first_result_header()
