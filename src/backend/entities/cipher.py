from typing import Literal
from enum import IntEnum

from .key import Key
from .message import Message


class CipherMode(IntEnum):
    ENCRYPT = 1
    DECRYPT = -1


class Cipher:

    _ALPHABETS = {
        'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
        'en': 'abcdefghijklmnopqrstuvwxyz'
    }

    def __init__(self,
                 message: Message,
                 key: Key,
                 action: Literal['encrypt', 'decrypt'] = 'encrypt') -> None:
        self._actions = {
            'encrypt': self._encrypt,
            'decrypt': self._decrypt
        }
        if action not in self._actions:
            raise ValueError(f'action must be one of [{', '.join(self._actions.keys())}]')
        if not isinstance(key, Key):
            raise TypeError('key must be of type Key')
        if not isinstance(message, Message):
            raise TypeError('message must be of type Message')
        if not (key.language == message.language):
            raise ValueError('key and message must be of the same language')
        if len(key.value) > len(message.value):
            raise ValueError('key must be less than or equal to message')
        self._message = message
        self._key = key
        self._expanded_key = self._expand_key(key, len(message.value))
        self._lang = key.language
        self._value = self._actions[action]()

    @property
    def message(self) -> Message:
        return self._message

    @property
    def key(self) -> Key:
        return self._key

    @property
    def expanded_key(self) -> Key:
        return self._expanded_key

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._lang

    @property
    def value(self) -> str:
        return self._value

    def _encrypt(self) -> str:
        return self._make_cipher(CipherMode.ENCRYPT)

    def _decrypt(self) -> str:
        return self._make_cipher(CipherMode.DECRYPT)

    def _make_cipher(self, mode: CipherMode) -> str:
        result = list()
        msg = self._message.value
        key = self._expanded_key.value
        alphabet = self._get_alphabet(self._lang)
        alphabet_len = len(alphabet)
        char_to_idx = {char: i for i, char in enumerate(alphabet)}
        for m_char, k_char in zip(msg, key):
            m_idx = char_to_idx.get(m_char)
            k_idx = char_to_idx.get(k_char) * mode.value
            new_idx = (m_idx + k_idx) % alphabet_len
            result.append(alphabet[new_idx])
        return ''.join(result)

    @staticmethod
    def _expand_key(key: Key, message_len: int) -> Key:
        """
        Increase the key length to the given message length by repetition.
        Args:
            key (Key): The key to increase.
            message_len (int): The message length.
        Returns:
            Key: The increased key.
        """
        key_value = key.value
        key_len = len(key_value)
        capacity = message_len // key_len
        rest = message_len % key_len
        new_key = key_value * capacity + key_value[:rest]
        return Key(new_key, lang=key.language)

    @staticmethod
    def _get_alphabet(language: Literal['ru', 'en']) -> str:
        return Cipher._ALPHABETS.get(language)
