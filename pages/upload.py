import pyautogui
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage
from driver_core.browser import Browser
from logger_params.logger import Logger
import time


class UploadsPage(BasePage):
    UNIQUE_ELEMENT_LOC = 'drag-drop-upload'
    INPUT_FILE_BTN = 'file-upload'
    SUBMIT_UPLOAD_BTN = 'file-submit'

    LABEL_PAGE_UPLOAD = '//*[contains(text(), "File Uploaded!")]'
    FILE_NAME_LABEL = 'uploaded-files'


    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Upload Page'
        self.unique_element = Label(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Уникальный элемент страницы'
        )
        self.input_file_button = Button(
            self.browser,
            self.INPUT_FILE_BTN,
            description='Кнопка загрузки'
        )
        self.submit_btn_upload = Button(
            self.browser,
            self.SUBMIT_UPLOAD_BTN,
            description='Кнопка подтверждения загрузки'
        )
        self.label_file_page = Label(
            self.browser,
            self.LABEL_PAGE_UPLOAD,
            description='Файл загружен'
        )
        self.file_name = Label(
            self.browser,
            self.FILE_NAME_LABEL,
            description='Название файла'
        )

    def upload_file(self, path_file: str, manual_upload: bool = False):
        if manual_upload:
            Logger.info('Ручной использование')
            self.input_file_button.js_click()
            time.sleep(4)
            pyautogui.write(path_file)
            time.sleep(3)
            pyautogui.press("enter")
            time.sleep(3)
        else:
            Logger.info(f'Загружен файл {path_file}')
            self.input_file_button.send_keys(path_file)

    def tap_upload_btn(self):
        self.submit_btn_upload.click()

    @property
    def get_text_success_page(self):
        text = {self.label_file_page.get_text(): self.file_name.get_text()}
        return text



