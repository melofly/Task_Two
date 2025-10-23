from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label
from logger_params.logger import Logger


class JavaScriptAlertsPage(BasePage):
    RESULT_LOCATOR = "result"
    JS_ALERT_BTN = '//*[@onclick="jsAlert()"]'
    JS_CONFIRM_BTN = "//*[@onclick='jsConfirm()']"
    JS_PROMPT_BTN = "//*[@onclick='jsPrompt()']"
    UNIQUE_ELEMENT_LOC = RESULT_LOCATOR

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "JavaScript Alerts Page"
        self.result = Label(browser, self.RESULT_LOCATOR, "Результат")
        self.alert_btn = Button(browser, self.JS_ALERT_BTN, "Кнопка JS Alert")
        self.confirm_btn = Button(browser, self.JS_CONFIRM_BTN, "Кнопка JS Confirm")
        self.prompt_btn = Button(browser, self.JS_PROMPT_BTN, "Кнопка JS Prompt")
        self.unique_element = self.result

    def click_js_alert(self):
        Logger.info(f"{self}: нажимаем на кнопку JS Alert")
        self.alert_btn.click()
        alert = self.browser.switch_to_alert()
        text = alert.text
        Logger.info(f"{self}: текст алерта = '{text}'")
        alert.accept()
        result_text = self.result.get_text()
        Logger.info(f"{self}: результат = '{result_text}'")
        return text, result_text

    def click_js_confirm(self, accept: bool = True):
        Logger.info(f"{self}: нажимаем на кнопку JS Confirm")
        self.confirm_btn.click()
        alert = self.browser.switch_to_alert()
        text = alert.text
        Logger.info(f"{self}: текст алерта = '{text}'")

        if accept:
            Logger.info(f"{self}: принимаем алерт")
            alert.accept()
        else:
            Logger.info(f"{self}: отклоняем алерт")
            alert.dismiss()

        result_text = self.result.get_text()
        Logger.info(f"{self}: результат = '{result_text}'")
        return text, result_text

    def click_js_prompt(self, input_text: str):
        Logger.info(f"{self}: нажимаем на кнопку JS Prompt")
        self.prompt_btn.click()

        alert = self.browser.switch_to_alert()
        text = alert.text
        Logger.info(f"{self}: текст алерта = '{text}'")

        Logger.info(f"{self}: вводим текст = '{input_text}'")
        alert.send_keys(input_text)
        alert.accept()

        result_text = self.result.get_text()
        Logger.info(f"{self}: результат = '{result_text}'")

        return text, result_text
