from elements.image import Image
from elements.label import Label
from pages.base_page import BasePage
from driver_core.browser import Browser
from logger_params.logger import Logger
from elements.web_element import WebElement

class HoversPage(BasePage):
    USERS_PROFILE = '//*[contains(@class, "figure")]'
    UNIQUE_ELEMENT_LOC = '//*[contains(text(), "Hovers")]'
    USERS_DESC = "//*[contains(@class, 'figcaption')]"
    USERS_DESC_NAME = "//*[contains(@class, 'figure')]//h5"
    USERS_DESC_LINK = "//*[contains(@href, 'users')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Hovers Page'

        self.unique_element = Label(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Уникальный элемент страницы (фигуры пользователей)'
        )

        self.users_profile = Image(
            browser=self.browser,
            locator=self.USERS_PROFILE,
            description='Профили пользователей (аватары)'
        )

        self.users_desc_name = Label(
            browser=self.browser,
            locator=self.USERS_DESC_NAME,
            description='Имя пользователя под аватаром'
        )

        self.users_link_profile = WebElement(
            browser=self.browser,
            locator=self.USERS_DESC_LINK,
            description='Ссылка на профиль пользователя'
        )

    def get_user_profile_element(self, index: int, desc: str = 'Профиль пользователя'):
        loc = f"{self.USERS_PROFILE}[{index}]"
        return WebElement(browser=self.browser, locator=loc, description=f"{desc} #{index}")

    def get_user_name_element(self, index: int, desc: str = 'Имя пользователя'):
        loc = f"//*[contains(@class, 'figure')][{index}]//h5"
        return WebElement(browser=self.browser, locator=loc, description=f"{desc} #{index}")

    def get_user_link_element(self, index: int, desc: str = 'Ссылка на профиль пользователя'):
        loc = f"//*[contains(@class, 'figure')][{index}]//a"
        return WebElement(browser=self.browser, locator=loc, description=f"{desc} #{index}")

    def hover_on_user(self, index: int):
        el = self.get_user_profile_element(index)
        el.hover()
        Logger.info(f"{self}: наведены на профиль пользователя #{index}")

    def get_user_name(self, index: int) -> str:
        el = self.get_user_name_element(index)
        text = el.get_text()[6:]
        Logger.info(f'{self}: имя юзера - {text}')
        return text

    def click_user_profile_link(self, index: int):
        el = self.get_user_link_element(index)
        el.click()
        current_url = self.browser.get_current_url
        Logger.info(f'{self}: переход на {current_url}')
