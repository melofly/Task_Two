from pages.base_page import BasePage
from elements.label import Label


class BasicAuthPage(BasePage):
    TEXT_LOCATOR = "//*[contains(@class, 'example')]//p"
    UNIQUE_ELEMENT_LOC = TEXT_LOCATOR

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Auth success message")

    def get_message(self) -> str:
        message = Label(self.browser, self.TEXT_LOCATOR, "Текст")
        return message.get_text()