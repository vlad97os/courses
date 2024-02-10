from pages.bag import BagPage
from pages.product import ProductPage
from pages.product_group import ProductGroupPage
from pages.store import StorePage


def test_add_to_bag(browser, start_page):
    start_page.open_store()
    store_page = StorePage(browser)
    store_page.open_product_group()
    product_group_page = ProductGroupPage(browser)
    product_group_page.open_product()
    product_page = ProductPage(browser)
    product_title_product_page = product_page.get_product_title()
    full_product_price_product_page = product_page.get_full_product_price()
    product_page.add_to_bag()
    bag_page = BagPage(browser)
    product_title_bag_page = bag_page.get_product_title()
    full_product_price_bag_page = bag_page.get_full_product_price()
    assert product_title_product_page == product_title_bag_page
    assert full_product_price_product_page == full_product_price_bag_page
    bag_page.remove_product()
