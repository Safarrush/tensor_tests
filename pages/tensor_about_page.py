from selenium.webdriver.common.by import By
from .base_page import BasePage


class TensorAboutPage(BasePage):
    URL = "https://tensor.ru/about"

    def go_to_site(self):
        self.open_url(self.URL)

    def find_work_section(self):
        images_selectors = [
            'img[alt*="Разрабатываем систему СБИС"]',
            'img[alt*="Продвигаем сервисы"]',
            'img[alt*="Создаем инфраструктуру"]',
            'img[alt*="Сопровождаем клиентов"]'
        ]
        width_height = []
        for selector in images_selectors:
            width_height.append(self.find_elem((
                By.CSS_SELECTOR, selector)))
        return width_height
