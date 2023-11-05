from selenium.webdriver.common.by import By

from configuration import (CSS_SELECTOR_COOKIE_INFO, DETAILS_BUTTON_LINK,
                           TENSOR_HOME_URL, XPATH_FIND_BLOCK)

from .base_page import BasePage


class TensorPage(BasePage):
    """
    Класс главной страницы "Тензор".
    """

    def go_to_site(self):
        self.open_url(TENSOR_HOME_URL)

    def find_block(self):
        block = self.find_elem((
            By.XPATH, XPATH_FIND_BLOCK))
        return block.text

    def go_to_details(self):
        cookie_exit_button = self.find_elem(
            (By.CSS_SELECTOR, CSS_SELECTOR_COOKIE_INFO), time=10)
        self.click_element(cookie_exit_button)
        details_button = self.find_elements(
            (By.LINK_TEXT, DETAILS_BUTTON_LINK))
        details_button[2].click()
