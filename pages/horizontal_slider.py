from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from logger_params.logger import Logger


class HorizontalSliderPage(BasePage):
    SLIDER = "//*[@type='range']"
    VALUE_DISPLAY = "range"
    UNIQUE_ELEMENT_LOC = SLIDER

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Горизонтальный слайдер"

        self.slider = Input(browser, self.SLIDER, "Ползунок слайдера")
        self.value_display = Label(
            browser,
            self.VALUE_DISPLAY,
            "Отображаемое значение слайдера"
        )

        self.unique_element = self.slider

    @property
    def get_slider_properties(self):
        slider_el = self.slider.wait_for_presence()
        min_val = float(slider_el.get_attribute("min"))
        max_val = float(slider_el.get_attribute("max"))
        step = float(slider_el.get_attribute("step"))

        Logger.info(f"{self}: свойства слайдера: min={min_val}, max={max_val}, step={step}")
        return min_val, max_val, step

    def set_slider_value(self, target_value: float) -> float:
        min_val, max_val, step = self.get_slider_properties

        Logger.info(f"{self}: попытка установить значение {target_value}")

        if not (min_val <= target_value <= max_val):
            Logger.warning(f"{self}: значение {target_value} выходит за диапазон {min_val}-{max_val}")
            target_value = min(max(target_value, min_val), max_val)

        slider_element = self.slider.wait_for_clickable()
        slider_element.click()
        slider_element.send_keys(Keys.HOME)
        Logger.info(f"{self}: слайдер сброшен в минимальное положение ({min_val})")

        steps = int(round((target_value - min_val) / step))
        Logger.info(f"{self}: перемещаем слайдер на {steps} шагов")

        for _ in range(abs(steps)):
            slider_element.send_keys(Keys.ARROW_RIGHT if steps > 0 else Keys.ARROW_LEFT)

        value_text = self.value_display.get_text().strip()
        try:
            actual_value = float(value_text)
        except ValueError:
            Logger.error(f"{self}: не удалось преобразовать '{value_text}' в число")
            raise

        Logger.info(f"{self}: текущее значение слайдера = {actual_value}")
        return actual_value
