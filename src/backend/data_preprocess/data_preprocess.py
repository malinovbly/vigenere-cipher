import re
from pathlib import Path

from pathvalidate import is_valid_filename

from ..exceptions import InvalidFileExtensionException, InvalidFileNameException


SUPPORTED_FILE_EXTENSIONS = ['.txt']


def clear_string(string: str) -> str:
    pattern = r'[^a-zа-яё]'
    cleared_string = re.sub(pattern, '', string, flags=re.IGNORECASE)
    return cleared_string


def preprocess_file(file_path: str) -> str:
    _is_file_name_valid(file_path.split('/')[-1])
    _check_file_extension(file_path)
    result_string = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            string = file.readline()
            if len(string) == 0: break
            result_string += clear_string(string)
    return result_string.lower()


def _check_file_extension(file_path: str) -> bool:
    file_path = Path(file_path)
    if file_path.suffix.lower() not in SUPPORTED_FILE_EXTENSIONS:
        raise InvalidFileExtensionException(
            f'Неподдерживаемый тип файла: "{file_path.suffix}"'
        )
    return True


def _is_file_name_valid(file_name: str) -> bool:
    if not is_valid_filename(file_name):
        raise InvalidFileNameException(
            f'Невалидное имя файла "{file_name}"'
        )
    return True
