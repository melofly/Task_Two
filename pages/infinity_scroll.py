from logger_params.logger import Logger
from pages.base_page import BasePage
from elements.web_element import WebElement


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOCATOR = "//div[@class='jscroll-added']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Бесконечный скролл"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Infinite Scroll Header")
        self.paragraphs = WebElement(browser, self.PARAGRAPH_LOCATOR, "Text Paragraph")

    def _count_scroll_parg(self, age: int):
        return self.PARAGRAPH_LOCATOR + f'[{age}]'

    def scroll_cont(self, index: int = 22):
        specific_paragraph = WebElement(
            self.browser,
            self._count_scroll_parg(index),
            f"Paragraph #{index}"
        )
        specific_paragraph.scroll()
        Logger.info(f"Прокрутили до параграфа №{index}")

