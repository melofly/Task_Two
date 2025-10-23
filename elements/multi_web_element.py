from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .web_element import WebElement
from selenium.common.exceptions import TimeoutException, WebDriverException
from logger_params.logger import Logger
from config.config_reader import ConfigReader
from selenium.webdriver import ActionChains
from driver_core.browser import Browser

config = ConfigReader()

class MultiWebElement:
    def __init__(
            self,
            browser: Browser,
            locator_xpath: str,
            description: str = None,
            timeout: int = config.get('timeout')
    ):
        self._index = 1

        self.browser = browser
        self.timeout = timeout if timeout is not None else 10
        self.formatable_locator = locator_xpath
        self.description = description if description else str(locator_xpath)
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)

    def __iter__(self):
       self._index = 1
       return self

    def __next__(self):
        current_el = WebElement(
            browser=self.browser,
            locator=self.formatable_locator.format(index=self._index),
            description=f'{self}:{self.description}',
            timeout=self.timeout
        )

        if not current_el.is_exists():
            raise StopIteration
        self._index += 1
        return current_el

    def __str__(self):
        return f'{self}:[{self.description}]'

    def __repr__(self):
        return str(self)

