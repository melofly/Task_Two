from selenium.common.exceptions import WebDriverException as error
from logger_params.logger import Logger

from elements.base_element import BaseElement as Elements

class Input(Elements):
    def clear(self):
        el = self.wait_for_visible()

        try:
            el.clear()
            Logger.info(f'{self} очищен')
        except error:
            Logger.error(f'{self}: {error}')

    def js_clear(self):
        el = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script("arguments[0].value =  ''", el)

    def input_keys(self, text_for_input: str):
        el = self.wait_for_presence()

        try:
            self.clear()
            el.send_keys(text_for_input)
            Logger.info(f'{self} ввел {text_for_input}')
        except error:
            Logger.error(f"{self}: {error}")

    def js_send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.js_clear()

        el = self.wait_for_presence()
        Logger.info(f"{self}: js send keys = {keys}")
        self.browser.execute_script(
            "arguments[0].value =  'arguments[1]'",
                                    el, keys
        )