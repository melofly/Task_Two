import pytest
from logger_params.logger import Logger
from pages.new_window import NewWindowPage


@pytest.mark.usefixtures("browser")
def test_new_window(browser):
    url = "https://the-internet.herokuapp.com/windows"
    page = NewWindowPage(browser)
    Logger.info(f"Открываем страницу {page.page_name}")
    page.browser.open(url)
    page.wait_for_open()

    expected_tab_text = 'New Window'

    page.click_btn()
    page.browser.switch_to_tab(1)
    actual_tab_text = page.browser.get_title()

    assert actual_tab_text == expected_tab_text, (
        f"Prompt текст: expected='{expected_tab_text}', actual='{actual_tab_text}'"
    )

    page.browser.switch_to_tab(0)
    page.wait_for_open()
    page.click_btn()
    page.wait_for_open()
    page.browser.switch_to_tab(2)
    actual_text_new_window = page.get_new_window_text
    expected_text_new_window = 'New Window'

    assert actual_text_new_window == expected_text_new_window, (
        f"Prompt текст: expected='{expected_tab_text}', actual='{actual_tab_text}'"
    )

    page.browser.close()
    page.browser.switch_to_tab(1)
    page.browser.close()

    actual_tabs_value = page.browser.tabs_count()
    expected_tabs_value = 1

    assert actual_tabs_value == expected_tabs_value, (
        f"Prompt текст: expected='{actual_tabs_value}', actual='{expected_tabs_value}'"
    )
