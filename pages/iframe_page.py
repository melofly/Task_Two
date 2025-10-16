from elements.button import Button
from elements.image import Image
from elements.label import Label
from elements.link_label import LinkLabel
from pages.base_page import BasePage
from driver_core.browser import Browser
from logger_params.logger import Logger
from elements.web_element import  WebElement as El


class FramesPage(BasePage):

    NESTED_FRAMES_MENU_BTN = '//span[text()="Nested Frames"]'
    FRAMES_MENU_BTN = '//span[text()="Frames"]'
    MENU_ALERTS_BTN = '(//span[contains(@class, "group-header")])[3]'

    PARENT_FRAME = 'frame1'
    CHILD_FRAME = '//iframe[@srcdoc="<p>Child Iframe</p>"]'

    FRAME_ONE = PARENT_FRAME
    FRAME_TWO = 'frame2'

    FRAME_HEADING = 'sampleHeading'

    PARENT_TEXT_LOC = "//body[contains(text(), 'Parent frame')]"
    CHILD_TEXT_LOC = "//p[text()='Child Iframe']"

    UNIQUE_ELEMENT_LOC = MENU_ALERTS_BTN

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = El(
            browser,
            self.UNIQUE_ELEMENT_LOC,
            "Уникальный элемент страницы"
        )
        self.menu_open = Button(
            browser=self.browser,
            locator=self.MENU_ALERTS_BTN,
            description='раскрыл меню'
        )
        self.nested_frames_menu = Button(
            browser=self.browser,
            locator=self.NESTED_FRAMES_MENU_BTN,
            description='Кнопка в меню Nested Frames'
        )
        self.frames_menu = Button(
            browser=self.browser,
            locator=self.FRAMES_MENU_BTN,
            description='Конпка в меню Frames'
        )
        self.parent_frame = El(
            browser=self.browser,
            locator=self.PARENT_FRAME,
            description='Фрейм Parent'
        )
        self.parent_frame_text = Label(
            browser=self.browser,
            locator=self.PARENT_TEXT_LOC,
            description='Текст внутри Parent'
        )

        self.frame_one_on_frame_section = El(
            browser=self.browser,
            locator=self.FRAME_ONE,
            description='Текст внутри Frame1'
        )

        self.frame_two_on_frame_section = El(
            browser=self.browser,
            locator=self.FRAME_TWO,
            description='Текст внутри Frame2'
        )

        self.child_frame = El(
            browser=self.browser,
            locator=self.CHILD_FRAME,
            description='Фрейм Child'
        )
        self.child_frame_text = Label(
            browser=self.browser,
            locator=self.CHILD_TEXT_LOC,
            description='Текст внутри Child'
        )

        self.frame_text = Label(
            browser=self.browser,
            locator=self.FRAME_HEADING,
            description='Описание фрэйма'
        )




    def open_alers_menu(self):
        Logger.info('Открываем секции')
        self.menu_open.click()


    def go_to_nested_section(self):
        self.nested_frames_menu.click()
        Logger.info('Перешли в Nested Menu секцию')

    def go_to_frames_section(self):
        self.frames_menu.click()
        Logger.info('Перешли в Frames секцию')

    @property
    def text_in_parent_frame(self):
        Logger.info(f'Получаем текст из {self.parent_frame}')
        self.browser.switch_to_frame(self.parent_frame.wait_for_visible())
        text =  self.parent_frame_text.get_text()
        self.browser.switch_to_default_frame()
        return text

    @property
    def text_in_child_frame(self):
        Logger.info(f'Получаем текст из {self.child_frame}')
        self.browser.switch_to_frame(self.parent_frame.wait_for_visible())
        self.browser.switch_to_frame(self.child_frame.wait_for_visible())
        text = self.child_frame_text.get_text()
        self.browser.switch_to_default_frame()
        return text

    def get_text_in_frame(self, frame_id: int):
        Logger.info(f'Получаем текст из Фрэйма{frame_id}')
        if frame_id == 1:
            self.browser.switch_to_frame(self.frame_one_on_frame_section.wait_for_visible())
        else:
            self.browser.switch_to_frame(self.frame_two_on_frame_section.wait_for_visible())

        text = self.frame_text.get_text()
        self.browser.switch_to_default_frame()
        return text


