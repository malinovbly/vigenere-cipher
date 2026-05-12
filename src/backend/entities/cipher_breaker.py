from typing import Literal
from collections import Counter, defaultdict

from .alphabet import Alphabet
from .cipher import Cipher
from .key import Key
from .message import Message


class CipherBreaker:
    def __init__(self, ciphertext: Message) -> None:
        if not isinstance(ciphertext, Message):
            raise TypeError('ciphertext must be of type Message')
        self._ciphertext: Message = ciphertext
        self._language: Literal['ru', 'en'] = ciphertext.language
        self._key: Key = self._find_key()
        self._value: Message = Cipher(self._ciphertext, self._key, action='decrypt').value

    @property
    def ciphertext(self) -> Message:
        return self._ciphertext

    @property
    def key(self) -> Key:
        return self._key

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._language

    @property
    def value(self) -> Message:
        return self._value

    def _find_key(self) -> Key:
        ciphertext = self._ciphertext.value
        key_length = self._find_key_length()

        alphabet = Alphabet(self._language)
        letters = alphabet.alphabet
        frequencies = alphabet.frequencies

        found_key = ''

        for i in range(key_length):
            column = ciphertext[i::key_length]
            best_shift = self._find_best_shift_least_squares_method(column, letters, frequencies)
            found_key += alphabet[best_shift]

        return Key(found_key, self._language)

    @staticmethod
    def _find_best_shift_least_squares_method(
            column: str, alphabet: str, lang_frequencies: dict[str, float]) -> int:
        n = len(alphabet)
        best_shift = 0
        min_mse = float('inf')  # MSE - Mean Squared Error - Среднеквадратичная ошибка

        col_counts = Counter(column)
        total_chars = len(column)
        observed_frequencies = {char: col_counts[char] / total_chars for char in alphabet}

        for s in range(n):
            current_mse = 0

            for i in range(n):
                target_char = alphabet[i]
                actual_char = alphabet[(i + s) % n]
                diff = observed_frequencies[actual_char] - lang_frequencies[target_char]
                current_mse += diff ** 2

            if current_mse < min_mse:
                min_mse = current_mse
                best_shift = s

        return best_shift

    def _find_key_length(self):
        most_probable_lengths = self._find_most_probable_key_lengths()

        if not most_probable_lengths or most_probable_lengths == [1]:
            most_probable_lengths = list(range(2, 21))

        text = self._ciphertext.value
        key_lengths_to_ics = dict()
        for length in most_probable_lengths:
            key_lengths_to_ics[length] = self._get_average_ic(text, length)

        sorted_dict = sorted(key_lengths_to_ics.items(), key=lambda x: x[1], reverse=True)

        return sorted_dict[0][0]

    def _find_most_probable_key_lengths(self, max_assumed_length: int = 20) -> list[int]:
        text = self._ciphertext.value
        ngrams_to_distances = self._find_repeating_substrings_to_distances(text)

        all_distances = list()
        for dists in ngrams_to_distances.values():
            all_distances.extend(dists)

        if not all_distances:
            return [1]

        factors_counter = Counter()
        for dist in all_distances:
            for possible_len in range(2, max_assumed_length + 1):
                if dist % possible_len == 0:
                    factors_counter[possible_len] += 1

        most_probable_lengths = [com[0] for com in factors_counter.most_common(5)]
        return most_probable_lengths

    def _get_average_ic(self, ciphertext: str, key_length: int) -> float:
        columns = [ciphertext[i::key_length] for i in range(key_length)]
        ics = [self._calculate_ic(col) for col in columns]
        return sum(ics) / len(ics)

    @staticmethod
    def _calculate_ic(text: str) -> float:
        if len(text) < 2: return 0.0

        counts = Counter(text)
        n = len(text)

        # Формула индекса совпадений:
        # sum(f * (f - 1)) / (n * (n - 1)),
        # где f - частота буквы, n - длина текста
        numerator = sum(f * (f - 1) for f in counts.values())
        denominator = n * (n - 1)
        return numerator / denominator

    @staticmethod
    def _find_repeating_substrings_to_distances(
            text: str, min_len: int = 3, max_len: int = 10):
        repeats = defaultdict(list)
        text_length = len(text)

        for length in range(min_len, max_len + 1):
            for i in range(text_length - length + 1):
                substring = text[i:i + length]
                repeats[substring].append(i)

        filtered_repeats = {
            sub: CipherBreaker._calc_distances(indexes)
            for sub, indexes in repeats.items()
            if len(indexes) > 1
        }

        return filtered_repeats

    @staticmethod
    def _calc_distances(indexes: list[int]) -> list[int]:
        distances = list()
        for i in range(1, len(indexes)):
            distances.append(indexes[i] - indexes[i - 1])
        return distances
