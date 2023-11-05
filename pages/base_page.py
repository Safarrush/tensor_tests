import os

import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import DOWNLOAD_DIRECTORY, DOWNLOADED_FILE_PATH


class BasePage:
    """
    Класс базовых функций для работы с страницами.
    """

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_elem(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(
            self.driver, time
        ).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, element):
        element.click()

    def execute_script(self, script, element):
        self.driver.execute_script(script, element)

    def download_file(self, download_link):
        file_url = download_link.get_attribute("href")

        if not os.path.exists(DOWNLOAD_DIRECTORY):
            os.makedirs(DOWNLOAD_DIRECTORY)

        response = requests.get(file_url, stream=True)

        with open(DOWNLOADED_FILE_PATH, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
