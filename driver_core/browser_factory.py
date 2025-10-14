from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from driver_core.browser import Browser
from config.config_reader import ConfigReader
from logger_params.logger import Logger

config = ConfigReader('/Users/melodinero/PycharmProjects/Task_Two/config/config.json')


class BrowserFactory:
    @staticmethod
    def create_browser(headless: bool = True) -> Browser:
        driver: WebDriver
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
            options.add_argument('--window-size=1920,1080')
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

        Logger.info(f"Создан браузер")
        return Browser(driver, timeout=config.get('timeout'))
