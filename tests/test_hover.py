import pytest
from logger_params.logger import Logger
from pages.hovers import HoversPage


@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize(
    "index",
        (
            1, 2, 3
        )
)
def test_hovers(browser, index):
    url = "https://the-internet.herokuapp.com/hovers"
    page = HoversPage(browser)

    Logger.info(f"Открываем страницу {page.page_name}")
    page.browser.open(url)
    page.wait_for_open()
    page.hover_on_user(index=int(index))

    expected_text = f'user{index}'
    actual_text = page.get_user_name(index=int(index))

    assert expected_text == actual_text, (
        f"Prompt текст: expected='{expected_text}', actual='{actual_text}'"
    )

    expected_url = f'https://the-internet.herokuapp.com/users/{index}'

    page.click_user_profile_link(index=index)
    actual_url = page.browser.driver.current_url

    assert expected_url == actual_url, (
        f"Prompt текст: expected='{expected_text}', actual='{actual_text}'"
    )











