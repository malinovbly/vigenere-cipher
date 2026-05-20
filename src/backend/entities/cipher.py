from typing import Literal
from enum import IntEnum

from .key import Key
from .message import Message
from .alphabet import Alphabet


class Cipher:

    class _CipherMode(IntEnum):
        ENCRYPT = 1
        DECRYPT = -1

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
            raise ValueError('Ключ не может быть длиннее сообщения!')
        self._message: Message = message
        self._key: Key = key
        self._expanded_key: Key = self._expand_key(key, len(message.value))
        self._language: Literal['ru', 'en'] = key.language
        self._value: Message = Message(self._actions[action](), self._language)

    @property
    def message(self) -> Message:
        return self._message

    @property
    def key(self) -> Key:
        return self._key

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._language

    @property
    def value(self) -> Message:
        return self._value

    def _encrypt(self) -> str:
        return self._make_cipher(self._CipherMode.ENCRYPT)

    def _decrypt(self) -> str:
        return self._make_cipher(self._CipherMode.DECRYPT)

    def _make_cipher(self, mode: _CipherMode) -> str:
        result = list()

        msg = self._message.value
        key = self._expanded_key.value

        alphabet = Alphabet(language=self._language)
        alphabet_len = len(alphabet)
        char_to_idx = alphabet.char_to_index_dict

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
        return Key(new_key, language=key.language)
