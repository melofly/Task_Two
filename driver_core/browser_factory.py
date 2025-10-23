from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from driver_core.browser import Browser
from config.config_reader import ConfigReader
from logger_params.logger import Logger

config = ConfigReader()


class BrowserFactory:
    @staticmethod
    def create_browser(headless: bool = True) -> Browser:
        driver: WebDriver
        options = ChromeOptions()
        if headless:
            options.add_argument(config.get(key="headless", root_key="options"))
            options.add_argument(config.get(key="size_window", root_key="options"))
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

        Logger.info(f"Создан браузер")
        return Browser(driver, timeout=config.get('timeout'))
