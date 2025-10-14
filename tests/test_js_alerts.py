import random
import string
import pytest
from pages.alerts_js import JavaScriptAlertsPage
from logger_params.logger import Logger

@pytest.mark.usefixtures("browser")
def test_javascript_alerts(browser):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    Logger.info("Открываем главную страницу JS Alerts")
    browser.open(url)

    page = JavaScriptAlertsPage(browser)
    page.wait_for_open()
    Logger.info("Страница успешно открыта")

    # ---------------- JS Alert ----------------
    actual_text, actual_result = page.click_js_alert()
    expected_alert_text = "I am a JS Alert"
    expected_result_text = "You successfully clicked an alert"

    assert actual_text == expected_alert_text, f"Alert текст: expected='{expected_alert_text}', actual='{actual_text}'"
    assert actual_result == expected_result_text, f"Result текст: expected='{expected_result_text}', actual='{actual_result}'"
    Logger.info("JS Alert проверен успешно")

    # ---------------- JS Confirm ----------------
    actual_text, actual_result = page.click_js_confirm(accept=True)
    expected_alert_text = "I am a JS Confirm"
    expected_result_text = "You clicked: Ok"

    assert actual_text == expected_alert_text, f"Confirm текст: expected='{expected_alert_text}', actual='{actual_text}'"
    assert actual_result == expected_result_text, f"Result текст: expected='{expected_result_text}', actual='{actual_result}'"
    Logger.info("JS Confirm проверен успешно")

    # ---------------- JS Prompt ----------------
    random_text = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    actual_text, actual_result = page.click_js_prompt(random_text)
    expected_alert_text = "I am a JS prompt"
    expected_result_text = f"You entered: {random_text}"

    assert actual_text == expected_alert_text, (f"Prompt текст: expected='{expected_alert_text}', actual='{actual_text}'")
    assert actual_result == expected_result_text, (f"Result текст: expected='{expected_result_text}', actual='{actual_result}'")
    Logger.info("JS Prompt проверен успешно")
