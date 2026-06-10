import os
import sys
import tkinter
from tkinter import ttk, messagebox
from enum import StrEnum

from .enums import LabelTexts, ButtonTexts, RadioButtonTexts, Language
from .base_widgets import create_frame, create_label, create_entry, create_text
from .models import SaveDataModel
from .utils import select_file, get_result, clear_string
from ..backend.exceptions import InvalidFileExtensionException


class Page(StrEnum):
    MAIN = 'MAIN'
    ENCRYPT = 'ENCRYPT'
    DECRYPT = 'DECRYPT'
    BREAK = 'BREAK'
    RESULT = 'RESULT'


class App(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self._config()
        self._current_page: Page = Page.MAIN
        self._previous_page: Page = Page.MAIN
        self._saved_data: SaveDataModel = SaveDataModel()
        self._create_main_page()

    #region Config

    def _config(self):
        self._setup_hotkeys()

        self.title('Шифр Виженера')

        self.resizable(False, False)
        self.geometry('900x600')

        icon_path = self._resource_path('src/frontend/static/icon.png')
        icon = tkinter.PhotoImage(file=icon_path)
        self.iconphoto(False, icon)

    def _setup_hotkeys(self):
        def keypress(e):
            if e.keycode == 86 and e.keysym != 'v':
                self._handle_clipboard('<<Paste>>')
            elif e.keycode == 67 and e.keysym != 'c':
                self._handle_clipboard('<<Copy>>')
            elif e.keycode == 88 and e.keysym != 'x':
                self._handle_clipboard('<<Cut>>')
        self.bind('<Control-KeyPress>', keypress)

    def _handle_clipboard(self, event_name):
        widget = self.focus_get()
        if hasattr(widget, 'event_generate'):
            widget.event_generate(event_name)

    @staticmethod
    def _resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)

    #endregion

    #region Pages

    def _create_main_page(self):
        frame = self._add_main_frame()

        self._add_main_label_frame(
            frame,
            LabelTexts.MainWindowLabel,
            label_options={'font': ('Roboto', 20)}
        )
        self._add_main_label_frame(
            frame,
            LabelTexts.MainWindowDescription,
        )
        self._add_main_label_frame(
            frame,
            LabelTexts.ChooseAction,
        )

        buttons_frame = create_frame(frame)
        self._add_main_menu_button(
            buttons_frame,
            ButtonTexts.EnterEncryptWindow,
            Page.ENCRYPT
        )
        self._add_main_menu_button(
            buttons_frame,
            ButtonTexts.EnterDecryptWindow,
            Page.DECRYPT
        )
        self._add_main_menu_button(
            buttons_frame,
            ButtonTexts.EnterBreakWindow,
            Page.BREAK
        )

    def _create_encrypt_page(self, with_insert_data=False):
        frame = self._add_main_frame()
        self._add_main_label_frame(
            frame,
            LabelTexts.EncryptWindow,
            label_options={'font': ('Roboto', 20)}
        )

        language = self._add_choose_lang_frame(frame)
        key = self._add_enter_key_frame(frame)
        message = self._add_enter_msg_frame(frame, LabelTexts.Message, cnt_per_frame=1, with_browse_button=True)

        if with_insert_data:
            key.insert(tkinter.INSERT, self._saved_data.key)
            message.insert(tkinter.INSERT, self._saved_data.message)

        buttons_frame = create_frame(frame)
        buttons_frame.pack_configure(side='bottom')
        self._add_get_result_button(
            buttons_frame,
            action='encrypt',
            language=language,
            message=message,
            key=key
        )
        self._add_return_button(buttons_frame, Page.MAIN)

    def _create_decrypt_page(self, with_insert_data=False):
        frame = self._add_main_frame()
        self._add_main_label_frame(
            frame,
            LabelTexts.DecryptWindow,
            label_options={'font': ('Roboto', 20)}
        )

        language = self._add_choose_lang_frame(frame)
        key = self._add_enter_key_frame(frame)
        message = self._add_enter_msg_frame(frame, LabelTexts.Message, cnt_per_frame=1, with_browse_button=True)

        if with_insert_data:
            key.insert(tkinter.INSERT, self._saved_data.key)
            message.insert(tkinter.INSERT, self._saved_data.message)

        buttons_frame = create_frame(frame)
        buttons_frame.pack_configure(side='bottom')
        self._add_get_result_button(
            buttons_frame,
            action='decrypt',
            language=language,
            message=message,
            key=key
        )
        self._add_return_button(buttons_frame, Page.MAIN)

    def _create_break_page(self, with_insert_data=False):
        frame = self._add_main_frame()
        self._add_main_label_frame(
            frame,
            LabelTexts.BreakWindow,
            label_options={'font': ('Roboto', 20)}
        )

        language = self._add_choose_lang_frame(frame)
        message = self._add_enter_msg_frame(frame, LabelTexts.Message, cnt_per_frame=1, with_browse_button=True)

        if with_insert_data:
            message.insert(tkinter.INSERT, self._saved_data.message)

        buttons_frame = create_frame(frame)
        buttons_frame.pack_configure(side='bottom')
        self._add_get_result_button(
            buttons_frame,
            action='break',
            language=language,
            message=message
        )
        self._add_return_button(buttons_frame, Page.MAIN)

    def _create_result_page(self):
        frame = self._add_main_frame()
        self._add_main_label_frame(
            frame,
            LabelTexts.Result,
            label_options={'font': ('Roboto', 20)}
        )

        try:
            data = self._saved_data
            key, message, result = get_result(
                data.action,
                language=data.language,
                message=data.message,
                key=data.key
            )
        except (InvalidFileExtensionException, ValueError, TypeError) as e:
            self._show_error(str(e))
            self._switch_page(self._previous_page)
            return

        _key = self._add_enter_key_frame(frame)
        _input = self._add_enter_msg_frame(frame, LabelTexts.Message, cnt_per_frame=2)
        _output = self._add_enter_msg_frame(frame, LabelTexts.Result, cnt_per_frame=2)

        _key.insert(tkinter.INSERT, key)
        _input.insert(tkinter.INSERT, message)
        _output.insert(tkinter.INSERT, result)

        buttons_frame = create_frame(frame)
        buttons_frame.pack_configure(side='bottom')
        self._add_return_button(buttons_frame, self._previous_page)

    #endregion

    #region Buttons

    def _add_return_button(self, frame, page_to_return: Page):
        button = ttk.Button(
            frame,
            text=ButtonTexts.Return,
            command=lambda: self._switch_page(_to=page_to_return, with_insert_data=True)
        )
        button.pack(side='right', anchor='s', padx=5, pady=5)

    def _add_main_menu_button(self, frame, text, page_to_go: Page):
        button = ttk.Button(
            frame,
            text=text,
            padding=5,
            command=lambda: self._switch_page(_to=page_to_go)
        )
        button.pack(fill='x', padx=25, pady=5)

    def _add_get_result_button(
            self, frame, action, language, message, key=None):
        button = ttk.Button(
            frame,
            text=ButtonTexts.Done,
            command=lambda: self._switch_page(
                _to=Page.RESULT,
                with_save=True,
                action=action,
                language=language,
                message=message,
                key=key
            )
        )
        button.pack(side='right', anchor='s', padx=5, pady=5)

    @staticmethod
    def _add_browse_button(frame, message_widget):
        button = ttk.Button(
            frame,
            text=ButtonTexts.ChooseFile,
            command=lambda: select_file(message_widget)
        )
        button.pack(side='right', padx=5, pady=5)

    #endregion

    #region Labels

    @staticmethod
    def _add_main_label_frame(parent, text, frame_options={}, label_options={}):
        frame = create_frame(parent, **frame_options)
        label = create_label(frame, text, False, padding=10, **label_options)
        label['width'] = ''
        label.pack()

    #endregion

    #region MessageBoxes

    def _show_error(self, msg: str):
        messagebox.showerror(
            title='Произошла ошибка',
            message=msg,
            parent=self
        )

    #endregion

    #region Frames

    def _add_main_frame(self):
        frame = ttk.Frame(self)
        frame.pack(fill='both', expand=True)
        return frame

    def _add_enter_msg_frame(
            self, parent, label_text: LabelTexts, cnt_per_frame=1, with_browse_button=False):
        frame = create_frame(parent)
        label = create_label(frame, label_text)
        entry = create_text(frame, cnt_per_frame)

        if with_browse_button:
            self._add_browse_button(frame, entry)

        return entry

    @staticmethod
    def _add_enter_key_frame(parent):
        frame = create_frame(parent)
        label = create_label(frame, LabelTexts.Key)
        entry = create_entry(frame)
        return entry

    @staticmethod
    def _add_choose_lang_frame(parent):
        frame = create_frame(parent)
        label = create_label(frame, LabelTexts.Language, width=25)

        radio_val = tkinter.StringVar(value=Language.RU)

        radio1 = ttk.Radiobutton(
            frame,
            text=RadioButtonTexts.LanguageRU,
            variable=radio_val,
            value=Language.RU
        )
        radio1.pack(side='left', padx=10, pady=5)

        radio2 = ttk.Radiobutton(
            frame,
            text=RadioButtonTexts.LanguageEN,
            variable=radio_val,
            value=Language.EN
        )
        radio2.pack(side='left')

        return radio_val

    #endregion

    #region Helpers

    def _switch_page(self, _to, with_insert_data=False, with_save=False, **data):
        if with_save:
            self._save_data(**data)

        self.winfo_children()[0].destroy()
        self._previous_page = self._current_page if self._current_page != Page.RESULT else self._previous_page

        match _to:
            case 'MAIN':
                self._create_main_page()
            case 'ENCRYPT':
                self._create_encrypt_page(with_insert_data)
            case 'DECRYPT':
                self._create_decrypt_page(with_insert_data)
            case 'BREAK':
                self._create_break_page(with_insert_data)
            case 'RESULT':
                self._create_result_page()

        self._current_page = _to

    def _save_data(self, action, language, message, key=None):
        prepared_data = {
            'action': action,
            'language': language.get(),
            'message': clear_string(message.get('1.0', 'end-1c')),
            'key': key.get() if key else None
        }
        self._saved_data = SaveDataModel(**prepared_data)

    # endregion
