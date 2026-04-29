import re
from pathlib import Path

from pathvalidate import is_valid_filename

from .exceptions import InvalidFileExtensionError


SUPPORTED_FILE_EXTENSIONS = ['.txt']


def clear_string(string: str) -> str:
    """Remove special characters and convert to lowercase."""
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
    """
    Check if file extension is processable.
    Args:
        file_path (str): Path to the file.
    Returns:
        bool: True if file extension is processable.
    Raises:
        InvalidFileExtensionError: File extension not supported.
    """
    file_path = Path(file_path)
    if file_path.suffix.lower() not in SUPPORTED_FILE_EXTENSIONS:
        raise InvalidFileExtensionError(f'Unsupported file extension: "{file_path.suffix}"')
    return True


def _is_file_name_valid(file_name: str) -> bool:
    """
    Check if file name contains special characters.
    Args:
        file_name (str): File name.
    Returns:
        bool: True if file name does not contain special characters.
    Raises:
        ValueError: File name is not valid.
    """
    if not is_valid_filename(file_name):
        raise ValueError(f'File name "{file_name}" is not valid.')
    return True
