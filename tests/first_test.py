import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage
import time

EXPEXTED_URL = "https://tensor.ru/about"
HEIGTH = 192
WIDTH = 270


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sbis_tensor_scenario(browser):
    sbis = SbisPage(browser)
    tensor = TensorPage(browser)
    sbis.go_to_contacts()
    sbis.find_tensor_banner()
    sbis.driver.switch_to.window(tensor.driver.window_handles[1])
    current_block = tensor.find_block()
    assert 'Сила в людях' == current_block, f"Элемент с текстом 'Сила в людях' не найден на странице."


def test_sbis_tensor_scenario_2(browser):
    tensor = TensorPage(browser)
    tensor.go_to_site()
    tensor.go_to_details()
    current_url = tensor.driver.current_url
    assert current_url == EXPEXTED_URL, f"Ожидался URL: {EXPEXTED_URL}, получен URL: {current_url}"


def test_sbis_tensor_scenario_3(browser):
    tensor_about = TensorAboutPage(browser)
    tensor_about.go_to_site()
    work_section = tensor_about.find_work_section()
    for work in work_section:
        height = int(work.get_attribute('height'))
        width = int(work.get_attribute('width'))
        assert height == HEIGTH and width == WIDTH, f"Ширина или высота не соответствует ожидаемой: {height}, высота: {width}"
