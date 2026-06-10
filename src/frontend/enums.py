from enum import StrEnum


class Language(StrEnum):
    RU = 'ru'
    EN = 'en'


class LabelTexts(StrEnum):
    EncryptWindow = 'Зашифровать сообщение'
    DecryptWindow = 'Расшифровать сообщение'
    BreakWindow = 'Взломать шифр'
    MainWindowDescription = ('С помощью данного приложения вы можете:\n'
                             ' - зашифровать текст,\n'
                             ' - расшифровать сообщение,\n'
                             ' - попытаться взломать шифр без ключа.')
    ChooseAction = 'Выберите, что необходимо сделать'
    Key = 'Ключ'
    Message = 'Сообщение'
    Result = 'Результат'
    Language = 'Алфавит'


class ButtonTexts(StrEnum):
    EnterEncryptWindow = 'Зашифровать сообщение'
    EnterDecryptWindow = 'Расшифровать сообщение'
    EnterBreakWindow = 'Взломать шифр'
    Return = 'Назад'
    Done = 'Готово'
    ChooseFile = 'Browse...'


class RadioButtonTexts(StrEnum):
    LanguageRU = 'Кириллица'
    LanguageEN = 'Латиница'
