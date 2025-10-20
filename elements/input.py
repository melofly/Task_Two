from selenium.common import TimeoutException
from elements.base_element import BaseElement as Elements
from logger_params.logger import Logger
import pyautogui

class Input(Elements):
    def send_keys(self, value: str):
        try:
            Logger.info(f'{self}: вставляем в поле {value}')
            return self.wait_for_clickable().send_keys(value)
        except TimeoutException:
            Logger.warning(f"{self}: произошла ошибка ввода")

    def manual_upload(self, path: str, press_btn: str):
        self.click()
        pyautogui.write(path)
        pyautogui.press(press_btn)

