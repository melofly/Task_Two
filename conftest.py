import pytest
from driver import DriverSingleton
from config.config_reader import ConfigReader

config = ConfigReader()

@pytest.fixture(scope="function")
def driver():
    driver = DriverSingleton().get_driver()
    driver.get(config.get('base_url'))
    yield driver
    DriverSingleton.quit()
