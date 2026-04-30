# vigenere-cipher


## Описание
Десктопное приложение, реализующее шифр Виженера.

Имеет следующие функции:
- Шифрование по ключу;
- Расшифрование по ключу;
- Взлом шифра без ключа.


## Запуск
1. Установка зависимостей
```bash
pip install -r requirements.txt
```

2. Создание исполняемого файла (.exe)
```bash
pyinstaller --onefile --windowed --icon="src/frontend/static/icon.ico" --add-data "src/frontend/static;src/frontend/static" --name="vigenere-cipher" run.py
```

3. Расположение исполняемого файла
```text
vigenere-cipher/
├── build/
├── dist/
│   └── vigenere-cipher.exe     # Итоговый исполняемый файл
├── src/
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
└── vigenere-cipher.spec
```
