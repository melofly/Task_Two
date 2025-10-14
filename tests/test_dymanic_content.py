import pytest
from pages.dynamic_content import DynamicContentPage
from logger_params.logger import Logger

@pytest.mark.usefixtures("browser")
def test_dynamic_content_images_match(browser):
    url = "https://the-internet.herokuapp.com/dynamic_content"
    page = DynamicContentPage(browser)

    Logger.info("Открываем страницу Dynamic Content")
    page.browser.open(url)
    page.wait_for_open()

    actual = False
    expected = True
    refresh_count = 0

    while actual is False:
        src_list = page.get_images_src()
        Logger.info(f"Обновление {refresh_count + 1}: {src_list}")

        if len(src_list) >= 2:
            if src_list[0] == src_list[1]:
                actual = True
            elif src_list[0] == src_list[2]:
                actual = True
            elif src_list[1] == src_list[2]:
                actual = True

        page.refresh_page()
        page.wait_for_open()
        refresh_count += 1

    assert actual == expected, (f"фактически совпадений нет после обновлений страницы")
    Logger.info(f"Найдены совпадающие изображения")
