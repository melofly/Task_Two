from pages.base_page import BasePage
from elements.web_element import WebElement as Element


class ContextMenuPage(BasePage):
    HOTSPOT_LOCATOR = "hot-spot"
    UNIQUE_ELEMENT_LOC = HOTSPOT_LOCATOR

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Context Menu"
        self.hotspot = Element(self.browser, self.HOTSPOT_LOCATOR, "Hotspot area")
        self.unique_element = self.hotspot


    def get_text_in_trigger(self):
        return self.hotspot.click(right_click=True, handle_alert=True)
