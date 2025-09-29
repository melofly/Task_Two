from selenium import webdriver

class DriverSinglton:
    _instance = None

    def __new__(cls):
        if DriverSinglton._instance is None:
            DriverSinglton._instance = super().__new__(cls)
            DriverSinglton._instance.driver = webdriver.Chrome()
            DriverSinglton._instance.driver.maximize_window()
        return DriverSinglton._instance

    def get_driver(self):
        return self.driver

