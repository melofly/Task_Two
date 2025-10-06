from selenium.webdriver.support.wait import WebDriverWait
from config.config_reader import ConfigReader

config = ConfigReader()

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get('timeout'))
        self.short_wait = WebDriverWait(
            driver,
            config.get('short_timeout'),
            poll_frequency=config.get('short_poll_frequency')
        )