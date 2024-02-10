from pages.choose_region import ChooseRegionPage


def test_current_region(start_page):
    assert start_page.get_current_region() == 'Belarus'


def test_change_region(browser, start_page):
    page_title = 'Apple (Maroc)'
    start_page.open_dropdown()
    start_page.click_other_country()
    start_page.click_continue()
    choose_region_page = ChooseRegionPage(browser)
    choose_region_page.click_region()
    assert browser.title == page_title
