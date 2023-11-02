from selenium.webdriver.common.by import By
from .base_page import BasePage


class TensorPage(BasePage):
    URL = "https://tensor.ru/"

    def go_to_site(self):
        self.open_url(self.URL)

    def find_block(self):
        block = self.find_elem((
            By.XPATH, '//*[contains(text(), "Сила в людях")]'))
        return block.text

    def go_to_details(self):
        cookie_exit_button = self.find_elem(
            (By.CSS_SELECTOR, 'div.tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.ws-flexbox.ws-align-items-center'), time=10)
        self.click_element(cookie_exit_button)
        details_button = self.find_elements((By.LINK_TEXT, 'Подробнее'))
        details_button[2].click()
