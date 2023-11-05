import shutil
import time

import allure

from configuration import (DOWNLOAD_DIRECTORY, DOWNLOADED_FILE_PATH,
                           EXPECTED_FILE_SIZE_MB)
from pages.sbis_download_page import SBISDownloadPage
from pages.sbis_page import SbisPage
from src.enums.global_enums import GlobalErrorMessages
from utils.file_operations import check_file_size, is_file_downloaded


@allure.feature("Страница скачивания приложения СБИС")
@allure.story("Проверка размера скачанного файла 'СБИС Плагин'")
def test_download_sbis_plugin(browser):
    """
    Проверка размера скачанного файла 'СБИС Плагин'.
    """
    sbis_page = SbisPage(browser)
    sbis_page.go_to_site()
    sbis_page.click_download_sbis_link()

    time.sleep(5)

    download_page = SBISDownloadPage(browser)
    time.sleep(5)
    download_page.click_download_sbis_plugin_button()
    download_page.click_download_button()

    assert (is_file_downloaded(
        DOWNLOADED_FILE_PATH
    )), GlobalErrorMessages.DOWNLOAD_ERROR.value
    assert (check_file_size(
        DOWNLOADED_FILE_PATH, EXPECTED_FILE_SIZE_MB)
    ), GlobalErrorMessages.SIZE_FILE_ERROR.value

    shutil.rmtree(DOWNLOAD_DIRECTORY)
