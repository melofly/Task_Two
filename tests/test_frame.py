import pytest
from logger_params.logger import Logger
from pages.iframe_page import FramesPage


@pytest.mark.usefixtures("browser")
def test_frames_and_nested_frames(browser):
    page = FramesPage(browser)
    url = "https://demoqa.com/frames"
    expected_parent = "Parent frame"
    expected_child = "Child Iframe"

    page.browser.open(url)
    page.wait_for_open()
    page.open_alers_menu()
    page.go_to_nested_section()
    actual_parent = page.text_in_parent_frame
    actual_child = page.text_in_child_frame

    page.open_alers_menu()
    page.go_to_frames_section()
    first_frame = page.get_text_in_frame(1)
    two_frame = page.get_text_in_frame(2)

    assert actual_parent == expected_parent, (
        f"Значение отображается некорректно: "
        f"expected={expected_parent}, actual={actual_parent}"

    )
    assert actual_child == expected_child, (
        f"Значение отображается некорректно: "
        f"expected={expected_parent}, actual={actual_parent}"
    )
    assert first_frame == two_frame, ('Значения не равны')


