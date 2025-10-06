from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.config_reader import ConfigReader

class DriverSingleton:
    _instance = None

    def __new__(cls, path_config=ConfigReader.PATH_JSON):
        if DriverSingleton._instance is None:
            DriverSingleton._instance = super().__new__(cls)

            config = ConfigReader(path_config)
            headless = config.get("headless", False)

            options = Options()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")

            DriverSingleton._instance.driver = webdriver.Chrome(options=options)
        return DriverSingleton._instance

    def get_driver(self):
        return self.driver

    @classmethod
    def quit(cls):
        if DriverSingleton._instance is not None:
            DriverSingleton._instance.driver.quit()
            DriverSingleton._instance = None
