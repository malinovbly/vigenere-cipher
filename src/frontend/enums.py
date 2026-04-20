from enum import StrEnum


class LabelTexts(StrEnum):
    EncryptWindow = 'Зашифровать сообщение по ключу'
    DecryptWindow = 'Расшифровать сообщение по ключу'
    BreakWindow = 'Взломать шифр'
    MainWindow = 'Шифр Виженера'
    Key = 'Ключ'
    Message = 'Сообщение'
    File = 'Файл'
    MessageWay = 'Способ ввода сообщения'


class ButtonTexts(StrEnum):
    EnterEncryptWindow = 'Зашифровать сообщение по ключу'
    EnterDecryptWindow = 'Расшифровать сообщение по ключу'
    EnterBreakWindow = 'Взломать шифр'
    Return = 'Назад'
    Done = 'Готово'
    ChooseFile = 'Browse...'
