import pytest
from pages.basic_auth import BasicAuthPage

url = "https://the-internet.herokuapp.com/basic_auth"

@pytest.mark.order(1)
@pytest.mark.parametrize(
    "username, password",
    [
        ("admin", "admin"),
    ]
)
def test_basic_auth(browser, username, password):
    page = BasicAuthPage(browser)
    browser.open_with_auth(url, username, password)
    page.wait_for_open()

    actual = page.get_message()
    expected = "Congratulations! You must have the proper credentials."

    assert expected == actual, (
        f"Упаль:\n"
        f"Ожидание: '{expected}'\n"
        f"Факт: '{actual}'"
    )