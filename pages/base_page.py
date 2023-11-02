from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_elem(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, element):
        element.click()

    def execute_script(self, script, element):
        self.driver.execute_script(script, element)

    def download_file(self, download_link):
        file_url = download_link.get_attribute("href")

        download_directory = os.path.join(os.getcwd(), "downloads")

        if not os.path.exists(download_directory):
            os.makedirs(download_directory)

        file_path = os.path.join(
            download_directory, "sbisplugin-setup-web.exe")
        response = requests.get(file_url, stream=True)

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
