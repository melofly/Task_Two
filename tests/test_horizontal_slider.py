import pytest
from pages.horizontal_slider import HorizontalSliderPage
from logger_params.logger import Logger
import random

@pytest.mark.usefixtures("browser")
class TestHorizontalSlider:

    def test_set_random_slider_value(self, browser):
        page = HorizontalSliderPage(browser)
        browser.open('http://the-internet.herokuapp.com/horizontal_slider')
        Logger.info("Открыта страница Горизонтального слайдера")

        min_val, max_val, step = page.get_slider_properties
        Logger.info(f"Диапазон слайдера: {min_val}–{max_val} (шаг {step})")

        values = [round(v, 1) for v in
                  [min_val + i * step for i in range(int((max_val - min_val) / step) + 1)]]
        random_value = random.choice([v for v in values if v not in (min_val, max_val)])

        Logger.info(f"Выбрано случайное значение для установки: {random_value}")

        actual_value = page.set_slider_value(random_value)

        assert actual_value == pytest.approx(random_value, rel=0.1), (
            f"Значение отображается некорректно: "
            f"expected={random_value}, actual={actual_value}"
        )

        Logger.info("Значение слайдера отображается корректно")
