from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SbisPage(BasePage):
    URL = "https://sbis.ru"

    def go_to_site(self):
        self.open_url(self.URL)

    def go_to_contacts(self):
        self.open_url(self.URL)
        contacts_button = self.find_elem((By.LINK_TEXT, "Контакты"))
        self.click_element(contacts_button)

    def find_tensor_banner(self):
        tensor_banner = self.find_elem(
            (By.CSS_SELECTOR, 'img[alt="Разработчик системы СБИС — компания «Тензор»"]'))
        self.click_element(tensor_banner)

    def defining_region(self):
        region_input = self.find_elem(
            (By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link'))
        partners2 = self.find_elem((
            By.CSS_SELECTOR, '.controls-BaseControl__viewContainer'))
        return region_input.text, partners2.text

    def click_download_sbis_link(self):
        download_sbis_link = self.find_elem(
            (By.LINK_TEXT, "Скачать СБИС"), time=10)
        self.execute_script(
            "arguments[0].scrollIntoView();", download_sbis_link)
        self.click_element(download_sbis_link)
