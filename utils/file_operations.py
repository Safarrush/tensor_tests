import os

import pytest


def is_file_downloaded(file_path):
    """
    Проверка, загружен ли файл.
    """
    return os.path.isfile(file_path)


def check_file_size(file_path, expected_size_mb, tolerance=1e-2):
    """
    Проверка размера файла.

    """
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    return pytest.approx(file_size, rel=tolerance) == expected_size_mb
