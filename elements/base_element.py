from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, WebDriverException
from logger_params.logger import Logger
from config.config_reader import ConfigReader
from selenium.webdriver import ActionChains
from driver_core.browser import Browser
import pyautogui


config = ConfigReader()

class BaseElement:
    def __init__(
            self,
            browser: Browser,
            locator: str,
            description: str = None,
            timeout: int = config.get('timeout')
    ):
        self.browser = browser
        self.timeout = timeout

        if "/" in locator:
            self.locator = (By.XPATH, locator)
        else:
            self.locator = (By.ID, locator)

        self.description = description if description else str(locator)
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self}: ожидаем {expected_condition.__name__}")
            return self._wait.until(expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: таймаут ожидания {expected_condition.__name__}")
            raise err

    def _wait_for_not(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self}: ожидаем, что {expected_condition.__name__} НЕ произойдет")
            return self._wait.until_not(expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: таймаут ожидания отрицательного условия {expected_condition.__name__}")
            raise err

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(EC.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(EC.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(EC.visibility_of_element_located)

    def send_keys(self, value: str):
        try:
            Logger.info(f'{self}: вставляем в поле {value}')
            return self.wait_for_clickable().send_keys(value)
        except TimeoutException:
            Logger.warning(f"{self}: произошла ошибка ввода")

    def is_exists(self) -> bool:
        try:
            self.wait_for_presence()
            Logger.info(f"{self}: элемент существует")
            return True
        except TimeoutException:
            Logger.warning(f"{self}: элемент не найден")
            return False

    def click(self, right_click: bool = False):
        element = self.wait_for_clickable()

        try:
            if right_click:
                Logger.info(f"{self}: правый клик по {self.description}")
                ActionChains(self.browser.driver).context_click(element).perform()
            else:
                Logger.info(f"{self}: обычный клик по {self.description}")
                element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: клик не удался - {err}")
            raise

    def js_click(self):
        el = self.wait_for_presence()

        try:
            self.browser.execute_script("arguments[0].click();", el)
            Logger.info(f"{self}: клик через JS выполнен")
        except WebDriverException as err:
            Logger.error(f"{self}: не удалось кликнуть через JS - {err}")
            raise

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: получение текста")
        try:
            text = element.text
            Logger.info(f"{self}: текст = '{text}'")
            return text
        except WebDriverException as err:
            Logger.error(f"{self}: не удалось получить текст - {err}")
            raise

    def get_attribute(
            self,
            name: str
    ) -> str:
        try:
            element = self.wait_for_presence()
            Logger.info(f"{self}: получение атрибута '{name}'")
            try:
                value = element.get_attribute(name)
                Logger.info(f"{self}: атрибут '{name}' = '{value}'")
                return value
            except WebDriverException as err:
                Logger.error(f"{self}: ошибка при получении атрибута — {err}")
                raise

    def get_css_property(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: получение CSS свойства '{name}'")
        try:
            value = element.value_of_css_property(name)
            Logger.info(f"{self}: CSS '{name}' = '{value}'")
            return value
        except WebDriverException as err:
            Logger.error(f"{self}: ошибка при получении CSS свойства - {err}")
            raise

    def hover(self):
        el = self.wait_for_visible()

        ActionChains(self.browser.driver).move_to_element(el).perform()
        Logger.info(f"{self}: наведение курсора на элемент")

    def manual_upload(self, path: str, press_btn: str):
        self.click()
        pyautogui.write(path)
        pyautogui.press(press_btn)


    def scroll(
            self,
            behavior: str = "smooth",
            block: str = "center",
    ):
        el = self.wait_for_presence()
        Logger.info(f"{self}: скролл")
        self.browser.execute_script(
            f"arguments[0].scrollIntoView({{ behavior: '{behavior}', block: '{block}' }});",
            el
        )
        return self
