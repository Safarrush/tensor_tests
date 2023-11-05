import os

SBIS_CONTACTS_URL = "https://sbis.ru/contacts/"
SBIS_HOME_URL = "https://sbis.ru"
TENSOR_ABOUT_URL = "https://tensor.ru/about"
TENSOR_HOME_URL = "https://tensor.ru/"

KEYWORD_URL = "moskva"
KEYWORD_TITLE = "Москва"
KEYWORD_REGION = "г. Москва"
KEYWORD_NEW_REGION = "Камчатский край"
KEYWORD_NEW_URL = "kamchatskij-kraj"
KEYWORD_NEW_TITLE = "Камчатский край"
PARTNER_KAMCHATKA_NAME = "СБИС - Камчатка"
PARTNER_MOSCOW_NAME = "СБИС - Москва"
CURRENT_BLOCK_NAME = "Сила в людях"

IMAGES_SELECTORS = [
    'img[alt*="Разрабатываем систему СБИС"]',
    'img[alt*="Продвигаем сервисы"]',
    'img[alt*="Создаем инфраструктуру"]',
    'img[alt*="Сопровождаем клиентов"]'
]

EXPECTED_FILE_SIZE_MB = 3.66

DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), "downloads")
DOWNLOADED_FILE_PATH = os.path.join(
    DOWNLOAD_DIRECTORY, "sbisplugin-setup-web.exe")

CSS_SELECTOR_SELECT_REGION = 'span.sbis_ru-Region-Chooser__text.sbis_ru-link'
CSS_SELECTOR_SELECT_KAMCHATSK = '[title="Камчатский край"]'
XPATH_DOWNLOAD_SBIS_PLUGIN_BUTTON = (
    "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']"
)
XPATH_DOWNLOAD_EXE_FILE = "//a[contains(text(), 'Скачать (Exe 3.66 МБ)')]"
CONTACTS_LINK = "Контакты"
CSS_SELECTOR_TENSOR_IMAGE_BANNER = (
    'img[alt="Разработчик системы СБИС — компания «Тензор»"]'
)
CSS_SELECTOR_REGION_CHOOSER = 'span.sbis_ru-Region-Chooser__text.sbis_ru-link'
CSS_SELECTOR_FIND_PARTNERS = '.controls-BaseControl__viewContainer'
DOWNLOAD_SBIS_BUTTON_LINK = "Скачать СБИС"
XPATH_FIND_BLOCK = '//*[contains(text(), "Сила в людях")]'
CSS_SELECTOR_COOKIE_INFO = (
    'div.tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.'
    'ws-flexbox.ws-align-items-center'
)
DETAILS_BUTTON_LINK = "Подробнее"

HEIGHT_IMAGE_ATTRIBUTE = "height"
WIDTH_IMAGE_ATTRIBUTE = "width"
