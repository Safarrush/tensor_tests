from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SbisPage(BasePage):
    URL = "https://sbis.ru"

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
        return region_input.text
        # self.click_element(region_input)
        # kamchatsk = self.find_elem(
        #     (By.CSS_SELECTOR, '[title="Камчатский край"]'))
        # self.click_element(kamchatsk)
        # region_input.send_keys(region)
        # region_input.send_keys(Keys.RETURN)
