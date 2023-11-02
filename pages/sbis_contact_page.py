from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SbisContactPage(BasePage):
    URL = "https://sbis.ru/contacts/"

    def go_to_site(self):
        self.open_url(self.URL)

    def select_region(self):
        region_input = self.find_elem(
            (By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link'))
        self.click_element(region_input)
        kamchatsk = self.find_elem(
            (By.CSS_SELECTOR, '[title="Камчатский край"]'), time=10)
        self.click_element(kamchatsk)
        # region_input.send_keys(region)
        # region_input.send_keys(Keys.RETURN)
