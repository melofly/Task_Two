import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as error_driver, TimeoutException
from config.config_reader import ConfigReader
from logger_params.logger import Logger

config = ConfigReader()

class Browser:
    def __init__(self, driver: WebDriver, timeout=config.get('timeout')):
        self._driver = driver
        self._driver.set_script_timeout(time_to_wait=config.get('page_load_timeout'))
        self._wait = WebDriverWait(driver=self._driver, timeout=timeout)
        self.main_handle = None

    @property
    def driver(self):
        return self._driver

    def open(self, url: str = config.get('base_url')):
        try:
            self._driver.get(url=url)
            Logger.info(f'{self}: открыл {url}')
            self.main_handle = self._driver.current_window_handle
        except error_driver:
            logging.error(f"{self}: {error_driver}")
            raise

    def open_with_auth(self, url: str, username: str, password: str):
        auth_url = url.replace(
            "https://",
            f"https://{username}:{password}@"
        )
        Logger.info(f"{self}: авторизован '{username}'")
        self.open(auth_url)

    def refresh(self):
        try:
            Logger.info(f"{self}: обновление страницы '{self._driver.current_url}'")
            self._driver.refresh()
        except error_driver:
            Logger.error(f"{self}: ошибка при обновлении страницы")
            raise

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def close(self):
        handles_count = len(self._driver.window_handles)

        try:
            if handles_count > 1:
                Logger.info(f"{self}: закрыл вкладку '{self._driver.current_window_handle}'")
                self._driver.close()
            else:
                self.quit()
        except error_driver:
            Logger.error(f"{self}: {error_driver}")
            raise

    def quit(self):
        try:
            Logger.info(f"{self}: закрыл браузер")
            self._driver.quit()
        except error_driver:
            Logger.error(f"{self}: {error_driver}")
            raise
        finally:
            self.main_handle = None

    @property
    def tabs_count(self):
        handles_count = len(self._driver.window_handles)
        Logger.info(f"{self}: открыто вкладок = {handles_count}")
        return handles_count

    def switch_to_tab(self, index: int):
        handles_count = self._driver.window_handles

        try:
            self._driver.switch_to.window(handles_count[index])
            Logger.info(f"{self}: переключился на вкладку #{index}")
        except IndexError:
            Logger.error(f"{self}: вкладка с индексом {index} не найдена")
            raise

    def wait_alert_present(self):
        Logger.info(f"{self}: ожидание alert")
        return self._wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        self.wait_alert_present()
        return self._driver.switch_to.alert

    def get_alert_text(self):
        text = self.switch_to_alert().text
        Logger.info(f"{self}: текст alert = '{text}'")
        return text

    def accept_alert(self):
        Logger.info(f"{self}: принять alert")
        self.switch_to_alert().accept()

    def send_keys_alert(self, text: str):
        Logger.info(f"{self}: отправить '{text}' в alert")
        self.switch_to_alert().send_keys(text)


    def switch_to_frame(self, frame):
        Logger.info(f"{self}: переключение во frame")
        return self._driver.switch_to.frame(frame)

    def switch_to_default_frame(self):
        Logger.info("Возврат из iframe в основной контент страницы")
        return self._driver.switch_to.default_content()

    def execute_script(self, script: str, *args):
        try:
            result = self._driver.execute_script(script, *args)
            Logger.info(f"{self}: выполнение скрипта '{script}' с аргументами {args}")
            return result
        except error_driver:
            Logger.error(f"{self}: ошибка при выполнении JS '{script}'")
            raise

    def save_screenshot(self, filename: str):
        try:
            self._driver.save_screenshot(filename)
            Logger.info(f"{self}: сохранение скриншота '{filename}'")
        except error_driver:
            Logger.error(f"{self}: {error_driver}")
            raise

    def get_title(self) -> str:
        title = self._driver.title
        Logger.info(f"{self}: заголовок текущей вкладки = '{title}'")
        return title

    def __str__(self):
        sid = getattr(self._driver, "session_id", None) or "no-session"
        return f'{self.__class__.__name__}[{sid}]'

    def __repr__(self):
        return str(self)
