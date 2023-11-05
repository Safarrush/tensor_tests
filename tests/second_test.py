import time

import allure

from configuration import (KEYWORD_NEW_REGION, KEYWORD_NEW_TITLE,
                           KEYWORD_NEW_URL, KEYWORD_REGION, KEYWORD_TITLE,
                           KEYWORD_URL, PARTNER_KAMCHATKA_NAME,
                           PARTNER_MOSCOW_NAME)
from pages.sbis_contact_page import SbisContactPage
from pages.sbis_page import SbisPage
from src.enums.global_enums import GlobalErrorMessages


@allure.feature("Главная страница СБИС")
@allure.story("Проверка корректности региона на странице контактов")
def test_current_region_on_sbis_contact_page(browser_with_proxy):
    """
    Проверка корректности определения региона на странице контактов.
    """
    sbis = SbisPage(browser_with_proxy)
    sbis.go_to_contacts()
    region = sbis.defining_region()
    time.sleep(3)
    assert (
        KEYWORD_URL in sbis.driver.current_url
    ), GlobalErrorMessages.NOT_CURRENT_URL.value
    assert (
        KEYWORD_TITLE in sbis.driver.title
    ), GlobalErrorMessages.NOT_CURRENT_TITLE.value
    assert (
        region[0] == KEYWORD_REGION
    ), GlobalErrorMessages.NOT_CURRENT_REGION.value
    assert (
        PARTNER_MOSCOW_NAME in region[1]
    ), GlobalErrorMessages.NOT_CURRENT_PARTNER.value


@allure.feature("Страница контактов СБИС")
@allure.story("Проверка смены региона на Камчатский край")
def test_defining_region_on_sbis_contact_page(browser_with_proxy):
    """
    Проверка смены региона на Камчатский край.
    """
    sbis_contact = SbisContactPage(browser_with_proxy)
    sbis = SbisPage(browser_with_proxy)
    sbis_contact.go_to_site()
    sbis_contact.select_region()
    time.sleep(5)
    region = sbis.defining_region()
    assert (
        KEYWORD_NEW_URL in sbis.driver.current_url
    ), GlobalErrorMessages.NOT_CURRENT_URL.value
    assert (
        KEYWORD_NEW_TITLE in sbis.driver.title
    ), GlobalErrorMessages.NOT_CURRENT_TITLE.value
    assert (
        region[0] == KEYWORD_NEW_REGION
    ), GlobalErrorMessages.NOT_CURRENT_REGION.value
    assert (
        PARTNER_KAMCHATKA_NAME in region[1]
    ), GlobalErrorMessages.NOT_CURRENT_PARTNER.value
