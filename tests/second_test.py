import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.sbis_contact_page import SbisContactPage
import time
from selenium.webdriver.chrome.options import Options

KEYWORD_URL = "moskva"
KEYWORD_TITLE = "Москва"
KEYWORD_REGION = "г. Москва"
KEYWORD_NEW_REGION = "Камчатский край"
KEYWORD_NEW_URL = "kamchatskij-kraj"
KEYWORD_NEW_TITLE = "Камчатский край"


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_extension('proxy.zip')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_sbis_tensor_scenario(browser):
    sbis = SbisPage(browser)
    sbis.go_to_contacts()
    region = sbis.defining_region()
    time.sleep(3)
    assert KEYWORD_URL in sbis.driver.current_url, f"Ожидался URL: {KEYWORD_URL}, получен URL : {sbis.driver.current_url}"
    assert KEYWORD_TITLE in sbis.driver.title, f"Ожидался title: {KEYWORD_TITLE}, получен title : {sbis.driver.title}"
    assert region[0] == KEYWORD_REGION, "Регион неверный, ожидался: {KEYWORD_REGION}, получен: {region}"
    assert "СБИС - Москва" in region[1], f"Неверные партнеры, ожидался: {'СБИС - Москва'}, получен: {region[1]}"


def test_sbis_tensor_scenario_2(browser):
    sbis_contact = SbisContactPage(browser)
    sbis = SbisPage(browser)
    sbis_contact.go_to_site()
    sbis_contact.select_region()
    time.sleep(5)
    region = sbis.defining_region()
    assert KEYWORD_NEW_URL in sbis.driver.current_url, f"Ожидался URL: {KEYWORD_NEW_URL}, получен URL : {sbis.driver.current_url}"
    assert KEYWORD_NEW_TITLE in sbis.driver.title, f"Ожидался title: {KEYWORD_NEW_TITLE}, получен title : {sbis.driver.title}"
    assert region[0] == KEYWORD_NEW_REGION, f"Регион неверный, ожидался: {KEYWORD_NEW_REGION}, получен: {region}"
    assert "СБИС - Камчатка" in region[1], f"Неверные партнеры, ожидался: {'СБИС - Камчатка'}, получен: {region[1]}"
