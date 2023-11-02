import os
import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.sbis_download_page import SBISDownloadPage
import time


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_download_sbis_plugin(driver):
    sbis_page = SbisPage(driver)
    sbis_page.go_to_site()

    sbis_page.click_download_sbis_link()
    time.sleep(5)
    download_page = SBISDownloadPage(driver)
    download_page.click_download_sbis_plugin_button()

    download_page.click_download_button()

    download_directory = os.path.join(os.getcwd(), "downloads")
    downloaded_file_path = os.path.join(
        download_directory, "sbisplugin-setup-web.exe")
    assert os.path.isfile(downloaded_file_path)
    file_size = os.path.getsize(downloaded_file_path)
    file_size_mb = file_size / (1024 * 1024)
    expected_file_size_mb = 3.66
    assert pytest.approx(file_size_mb, rel=1e-2) == expected_file_size_mb
    os.remove(downloaded_file_path)
