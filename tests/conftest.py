import os
import pytest
from logger_params.logger import Logger
from config.config_reader import ConfigReader
from driver_core.browser_factory import BrowserFactory
from driver_core.browser import Browser



@pytest.fixture(scope="session", autouse=True)
def prepare_logs():
    logs_dir = "logs"

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        Logger.info(f"Создана директория для логов: {logs_dir}")
    else:
        Logger.info(f"Директория логов уже существует: {logs_dir}")


@pytest.fixture(scope="function")
def browser():
    config = ConfigReader()
    headless = config.get("headless", True)
    Logger.info("Инициализация браузера через BrowserFactory")
    browser = BrowserFactory.create_browser(headless=headless)
    yield browser
    Logger.info("Закрытие браузера после теста")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        Logger.error(f"Тест упал: {item.name}")
        browser = item.funcargs.get("browser", None)
        if browser:
            screenshot_path = os.path.join("logs", f"{item.name}.png")
            try:
                browser.save_screenshot(screenshot_path)
                Logger.info(f"Скриншот сохранён: {screenshot_path}")
                Logger.info(f"URL на момент падения: {browser.driver.current_url}")
            except Exception as e:
                Logger.error(f"Ошибка при сохранении скриншота: {e}")
