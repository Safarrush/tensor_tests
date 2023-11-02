from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SBISDownloadPage(BasePage):

    def click_download_sbis_plugin_button(self):
        download_button = self.find_elem(
            (By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']"))
        self.execute_script("arguments[0].click();", download_button)
        self.click_element(download_button)

    def click_download_button(self):
        download_button = self.find_elem(
            (By.XPATH, "//a[contains(text(), 'Скачать (Exe 3.66 МБ)')]"))
        self.execute_script("arguments[0].click();", download_button)
        self.download_file(download_button)
