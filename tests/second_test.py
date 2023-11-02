import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.sbis_contact_page import SbisContactPage
from pages.tensor_about_page import TensorAboutPage
import time
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import pyautogui


@pytest.fixture(scope="function")
def browser():
    chrome_options = webdriver.ChromeOptions()
    proxy_helper = SeleniumAuthenticatedProxy(
        proxy_url="http://ZX67s4:odQXj2aXll@77.83.148.123:1050")
    proxy_helper.enrich_chrome_options(chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(2)
    pyautogui.press("enter")
    yield driver
    driver.quit()


def test_sbis_tensor_scenario(browser):
    sbis = SbisPage(browser)
    sbis.go_to_contacts()
    region = sbis.defining_region()
    assert region == "г. Москва", "Регион не верный"


def test_sbis_tensor_scenario_2(browser):
    sbis_contact = SbisContactPage(browser)
    sbis = SbisPage(browser)
    sbis_contact.go_to_site()
    sbis_contact.select_region()
    time.sleep(5)
    region = sbis.defining_region()
    assert region == "Камчатский край", "Регион не верный"
    # Check if the selected region is displayed
    # selected_region = sbis.driver.find_element(By.CSS_SELECTOR, '.input-box__input')
    #     assert selected_region.get_attribute('value') == target_region
    # sbis.driver.switch_to.window(tensor.driver.window_handles[1])
    # current_block = tensor.find_block()
    # assert 'Сила в людях' == current_block, f"Элемент с текстом 'Сила в людях' не найден на странице."
