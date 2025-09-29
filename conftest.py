import pytest
from driver import DriverSinglton

URL = "https://store.steampowered.com/"

@pytest.fixture(scope="session")
def driver():
    driver = DriverSinglton().get_driver()
    driver.get(URL)
    yield driver
    driver.quit()
