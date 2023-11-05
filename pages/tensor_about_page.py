from selenium.webdriver.common.by import By

from configuration import IMAGES_SELECTORS, TENSOR_ABOUT_URL
from pages.base_page import BasePage


class TensorAboutPage(BasePage):
    """
    Класс страницы "О тензоре".
    """

    def go_to_site(self):
        self.open_url(TENSOR_ABOUT_URL)

    def find_work_section(self):
        width_height = []
        for selector in IMAGES_SELECTORS:
            width_height.append(self.find_elem((
                By.CSS_SELECTOR, selector)))
        return width_height
