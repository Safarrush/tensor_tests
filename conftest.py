import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def browser_with_proxy():
    chrome_options = Options()
    chrome_options.add_extension('proxy.zip')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
