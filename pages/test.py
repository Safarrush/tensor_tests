from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import pyautogui

# Эмулируем нажатие клавиши "Enter"


chrome_options = webdriver.ChromeOptions()

# Initialize SeleniumAuthenticatedProxy
proxy_helper = SeleniumAuthenticatedProxy(
    proxy_url="http://ZX67s4:odQXj2aXll@77.83.148.123:1050")

# Enrich Chrome options with proxy authentication
proxy_helper.enrich_chrome_options(chrome_options)

# Start WebDriver with enriched options
driver = webdriver.Chrome(options=chrome_options)
pyautogui.press("enter")

driver.get("https://sbis.ru/contacts/")

# text = driver.find_element(
#     By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link')
# print(text.text)
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link')
)
element.click()
# region_input = driver.find_element(
#     By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
# region_input.click()
# time.sleep(3)
# kamchatsk = driver.find_element(
#     By.CSS_SELECTOR, '[title="Камчатский край"]')
# kamchatsk.click()
# time.sleep(3)
