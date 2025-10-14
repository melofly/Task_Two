import pytest
from pages.contex_menu import ContextMenuPage
from logger_params.logger import Logger

@pytest.mark.usefixtures("browser")
def test_context_menu_alert(browser):
    url = "https://the-internet.herokuapp.com/context_menu"
    Logger.info("Открываем страницу Context Menu")
    browser.open(url)

    page = ContextMenuPage(browser)
    page.wait_for_open()
    Logger.info("Страница успешно открыта")
    page.get_text_in_trigger()
    actual_alert_text = page.get_text_in_trigger()
    expected_alert_text = "You selected a context menu"

    assert actual_alert_text == expected_alert_text, (
        f"Alert текст не совпадает: expected='{expected_alert_text}', actual='{actual_alert_text}'"
    )
    Logger.info("Alert успешно проверен и закрыт")
