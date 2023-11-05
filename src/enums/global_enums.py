from enum import Enum


class GlobalErrorMessages(Enum):
    """
    Статусы ошибок.
    """
    NOT_FOUND = "Элемент не найден на странице."
    NOT_CURRENT_URL = "Ожидался иной URL."
    NOT_CURRENT_WIDTH_IMAGE = "Высота изображений не совпадает."
    NOT_CURRENT_HEIGTH_IMAGE = "Ширина изображений не совпадает."
    NOT_CURRENT_PARTNER = "Партнеры не совпадают."
    NOT_CURRENT_REGION = "Регион определен неверно."
    NOT_CURRENT_TITLE = "Ожидался иной title."
    DOWNLOAD_ERROR = "Проблемы с загрузкой файла."
    SIZE_FILE_ERROR = "Не совпадают размеры файла."
