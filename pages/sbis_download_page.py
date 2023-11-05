from selenium.webdriver.common.by import By

from configuration import (XPATH_DOWNLOAD_EXE_FILE,
                           XPATH_DOWNLOAD_SBIS_PLUGIN_BUTTON)
from pages.base_page import BasePage


class SBISDownloadPage(BasePage):
    """
    Класс страницы для скачивания приложений СБИС".
    """

    def click_download_sbis_plugin_button(self):
        download_button = self.find_elem(
            (By.XPATH, XPATH_DOWNLOAD_SBIS_PLUGIN_BUTTON))
        self.execute_script("arguments[0].click();", download_button)
        self.click_element(download_button)

    def click_download_button(self):
        download_button = self.find_elem(
            (By.XPATH, XPATH_DOWNLOAD_EXE_FILE))
        self.execute_script("arguments[0].click();", download_button)
        self.download_file(download_button)
