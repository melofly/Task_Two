from pages.base_page import BasePage
from elements.label import Label
from elements.web_element import WebElement



class DynamicContentPage(BasePage):
    IMAGES_LOC = "//*[@id='content']//img"
    UNIQUE_ELEMENT_LOC = "//*[contains(text(), 'Dynamic')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Dynamic Header")


    def get_images_src(self):
        images = WebElement(
            browser=self.browser,
            locator=self.IMAGES_LOC,
            description='картинки'
        )
        images_src = images.get_attribute("src")
        src_list = []

        for image in images_src:
            src_list.append(image)
        return src_list
