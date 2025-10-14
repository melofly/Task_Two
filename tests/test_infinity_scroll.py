import pytest
from pages.infinity_scroll import InfiniteScrollPage

url = "https://the-internet.herokuapp.com/infinite_scroll"

@pytest.mark.usefixtures('browser')
def test_basic_auth(browser):
    page = InfiniteScrollPage(browser)
    page.browser.open(url)
    page.wait_for_open()

    page.scroll_cont()

    assert 1 == 1