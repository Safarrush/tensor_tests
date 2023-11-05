import allure

from configuration import (CURRENT_BLOCK_NAME, HEIGHT_IMAGE_ATTRIBUTE,
                           TENSOR_ABOUT_URL, WIDTH_IMAGE_ATTRIBUTE)
from pages.sbis_page import SbisPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_page import TensorPage
from src.enums.global_enums import GlobalErrorMessages


@allure.feature("Главная страница СБИС")
@allure.story("Ищем блок 'Сила в людях'")
def test_find_block_on_tensor_page(browser):
    """
    Проверка наличия блока 'Сила в людях' на главной странице СБИС.
    """
    sbis = SbisPage(browser)
    tensor = TensorPage(browser)
    sbis.go_to_contacts()
    sbis.find_tensor_banner()
    sbis.driver.switch_to.window(tensor.driver.window_handles[1])
    block_name = tensor.find_block()
    assert (
        CURRENT_BLOCK_NAME == block_name
    ), GlobalErrorMessages.NOT_FOUND.value


@allure.feature("Главная страница Тензор")
@allure.story("Сравниваем url на странице tensor/about")
def test_current_url_on_tensor_about_page(browser):
    """
    Проверка url на странице tensor/about.
    """
    tensor = TensorPage(browser)
    tensor.go_to_site()
    tensor.go_to_details()
    current_url = tensor.driver.current_url
    assert (
        current_url == TENSOR_ABOUT_URL
    ), GlobalErrorMessages.NOT_CURRENT_URL.value


@allure.feature("Страница подробнее Тензор")
@allure.story("Проверяем размеры изображений на странице tensor/about")
def test_check_images_size_on_working_block(browser):
    """
    Проверка размеров изображений на странице tensor/about.
    """
    tensor_about = TensorAboutPage(browser)
    tensor_about.go_to_site()
    work_section = tensor_about.find_work_section()
    first_image = work_section[0]

    first_height = int(first_image.get_attribute(HEIGHT_IMAGE_ATTRIBUTE))
    first_width = int(first_image.get_attribute(WIDTH_IMAGE_ATTRIBUTE))

    for image in work_section[1:]:
        height = int(image.get_attribute(HEIGHT_IMAGE_ATTRIBUTE))
        width = int(image.get_attribute(WIDTH_IMAGE_ATTRIBUTE))

        assert (
            height == first_height
        ), GlobalErrorMessages.NOT_CURRENT_HEIGTH_IMAGE.value
        assert (
            width == first_width
        ), GlobalErrorMessages.NOT_CURRENT_WIDTH_IMAGE.value
