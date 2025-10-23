import pytest
from pages.infinity_scroll import InfiniteScrollPage

url = "https://the-internet.herokuapp.com/infinite_scroll"

@pytest.mark.usefixtures('browser')
@pytest.mark.parametrize('age',["22"])
def test_infinite_scroll(browser, age):
    page = InfiniteScrollPage(browser)
    page.browser.open(url)
    page.wait_for_open()

    page.scroll_count(index=age)

    assert True