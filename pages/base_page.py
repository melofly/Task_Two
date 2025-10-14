from logger_params.logger import Logger
from driver_core.browser import Browser

class BasePage:
     UNIQUE_ELEMENT_LOC = None

     def __init__(self, browser: Browser):
         self.browser = browser
         self.page_name = None
         self.unique_element = None

     def wait_for_open(self) -> None:
         Logger.info(f"{self}: ждет открытия")
         self.unique_element.wait_for_presence()

     def refresh_page(self):
         self.browser.refresh()

     def __str__(self) -> str:
         return f"{self.__class__.__name__}[{self.page_name}]"

     def __repr__(self) -> str:
         return str(self)