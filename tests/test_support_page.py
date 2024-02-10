from pages.detailed_information_support import DetailedInformationSupportPage


def test_limit_search_results(search_on_support_page):
    search_request = 'ID'
    max_number_of_search_results = 5
    search_on_support_page.input_in_search(search_request)
    assert search_on_support_page.get_number_of_search_results() == max_number_of_search_results


def test_display_quick_links(search_on_support_page, browser):
    number_of_quick_links = 5
    assert search_on_support_page.get_number_of_search_results() == number_of_quick_links
    first_quick_link = search_on_support_page.get_text_first_quick_link()
    search_on_support_page.click_first_quick_link()
    detailed_information_support_page = DetailedInformationSupportPage(browser)
    assert first_quick_link == detailed_information_support_page.get_title()
