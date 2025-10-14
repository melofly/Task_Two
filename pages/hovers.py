from elements.image import Image
from elements.label import Label
from elements.link_label import LinkLabel
from pages.base_page import BasePage
from driver_core.browser import Browser
from logger_params.logger import Logger
from elements.base_element import BaseElement as Element


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

        self.users_link_profile = LinkLabel(
            browser=self.browser,
            locator=self.USERS_DESC_LINK,
            description='Ссылка на профиль пользователя'
        )


    def _fast_gate_index(self, index: int, desc: str, purpose: str):
        if purpose == 'profile':
            loc = self.USERS_PROFILE + f'[{index}]'
            index_el = Element(browser=self.browser, locator=loc, description=f'{desc}{index}')
        elif purpose == 'name':
            loc = f"//*[contains(@class, 'figure')][{index}]//h5"
            index_el = Element(browser=self.browser, locator=loc, description=f'{desc}{index}')
        else:
            loc = f"//*[contains(@class, 'figure')][{index}]//a"
            index_el = Element(browser=self.browser, locator=loc, description=f'{desc}{index}')
        return index_el

    def hover_on_user(self, index: int, desc: str = 'наводимся на пользователя', purpose = 'profile'):
        el = self._fast_gate_index(index=index, desc=desc, purpose=purpose)
        Logger.info(f"{self}: наведены на профиль пользователя #{index}")
        el.hover()

    def get_user_name(self, index: int, desc: str = 'Имя юзера', purpose = 'name') -> str:
        el = self._fast_gate_index(index=index, desc=desc, purpose=purpose)
        text = el.get_text()[6:]
        Logger.info(f'{self}: имя юзера - {text}')
        return text

    def click_user_profile_link(self, index: int, desc: str = 'Ccылка на профиль', purpose = 'link'):
        el = self._fast_gate_index(index=index, desc=desc, purpose=purpose)
        el.click()
        current_url = self.browser.driver.current_url
        Logger.info(f'Переход на {current_url}')


