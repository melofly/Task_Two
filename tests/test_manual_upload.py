import pytest
from pages.upload import UploadsPage


@pytest.mark.usefixtures("browser")
def test_file_upload(browser):
    url = "https://the-internet.herokuapp.com/upload"
    browser.open(url)

    page = UploadsPage(browser)
    page.wait_for_open()

    expected_label = "File Uploaded!"
    expected_filename = "config.json"

    page.upload_file(
        "/config/config.json",
        manual_upload=True
    )
    page.tap_upload_btn()

    actual_label, actual_filename = next(iter(page.get_text_success_page.items()))

    assert actual_label == expected_label, f"Ожидали '{expected_label}', получили '{actual_label}'"
    assert actual_filename == expected_filename, f"Ожидали '{expected_filename}', получили '{actual_filename}'"
