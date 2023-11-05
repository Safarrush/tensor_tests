from selenium.webdriver.common.by import By

from configuration import (CSS_SELECTOR_SELECT_KAMCHATSK,
                           CSS_SELECTOR_SELECT_REGION, SBIS_CONTACTS_URL)
from pages.base_page import BasePage


class SbisContactPage(BasePage):
    """
    Класс страницы "СБИС Контакты".
    """

    def go_to_site(self):
        self.open_url(SBIS_CONTACTS_URL)

    def select_region(self):
        region_input = self.find_elem(
            (By.CSS_SELECTOR, CSS_SELECTOR_SELECT_REGION))
        self.click_element(region_input)
        kamchatsk_button = self.find_elem(
            (By.CSS_SELECTOR, CSS_SELECTOR_SELECT_KAMCHATSK), time=10)
        self.click_element(kamchatsk_button)
