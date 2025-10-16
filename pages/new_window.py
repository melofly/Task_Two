from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage
from driver_core.browser import Browser
from logger_params.logger import Logger


class NewWindowPage(BasePage):
    NEW_WINDOW_BTN = '//*[@target="_blank"]'
    UNIQUE_ELEMENT_LOC = '//*[contains(text(), "Opening a new window")]'
    NEW_WINDOW_TEXT = '//h3'


    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'New Window'
        self.unique_element = Label(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Уникальный элемент страницы'
        )
        self.new_window_btn = Button(
            browser=self.browser,
            locator=self.NEW_WINDOW_BTN,
            description='Кнопка перехода на новую страницу'
        )
        self.window_label = Label(
            browser=self.browser,
            locator=self.NEW_WINDOW_TEXT,
            description='текст'
        )

    def click_btn(self):
        self.new_window_btn.click()

    @property
    def get_new_window_text(self) -> str:
        text = self.window_label.get_text()
        Logger.info(f"{self}: текст в новом окне = '{text}'")
        return text
