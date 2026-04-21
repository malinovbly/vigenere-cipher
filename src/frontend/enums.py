from enum import StrEnum


class LabelTexts(StrEnum):
    EncryptWindow = 'Зашифровать сообщение по ключу'
    DecryptWindow = 'Расшифровать сообщение по ключу'
    BreakWindow = 'Взломать шифр'
    MainWindowDescription = ('Шифр Виженера - один из самых известных методов\n'
                             '  классической криптографии\n'
                             'Здесь вы можете:\n'
                             '  - зашифровать текст;\n'
                             '  - расшифровать сообщение по ключу;\n'
                             '  - попытаться взломать шифр без ключа')
    MainWindowChooseAction = 'Выберите, что необходимо сделать'
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


class RadioButtonTexts(StrEnum):
    Text = 'Текст'
    File = 'Файл (.txt)'
