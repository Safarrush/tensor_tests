from selenium.webdriver.common.by import By

from configuration import (CONTACTS_LINK, CSS_SELECTOR_FIND_PARTNERS,
                           CSS_SELECTOR_REGION_CHOOSER,
                           CSS_SELECTOR_TENSOR_IMAGE_BANNER,
                           DOWNLOAD_SBIS_BUTTON_LINK, SBIS_HOME_URL)
from pages.base_page import BasePage


class SbisPage(BasePage):
    """
    Класс главной страницы "СБИС".
    """

    def go_to_site(self):
        self.open_url(SBIS_HOME_URL)

    def go_to_contacts(self):
        self.open_url(SBIS_HOME_URL)
        contacts_button = self.find_elem((By.LINK_TEXT, CONTACTS_LINK))
        self.click_element(contacts_button)

    def find_tensor_banner(self):
        tensor_banner = self.find_elem(
            (By.CSS_SELECTOR, CSS_SELECTOR_TENSOR_IMAGE_BANNER))
        self.click_element(tensor_banner)

    def defining_region(self):
        region_input = self.find_elem(
            (By.CSS_SELECTOR, CSS_SELECTOR_REGION_CHOOSER))
        partners = self.find_elem((
            By.CSS_SELECTOR, CSS_SELECTOR_FIND_PARTNERS))
        return region_input.text, partners.text

    def click_download_sbis_link(self):
        download_sbis_link = self.find_elem(
            (By.LINK_TEXT, DOWNLOAD_SBIS_BUTTON_LINK), time=10)
        self.execute_script(
            "arguments[0].scrollIntoView();", download_sbis_link)
        self.click_element(download_sbis_link)
