import tkinter
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from ..backend.data_preprocess.exceptions import InvalidFileExtensionError
from .widgets.entries import create_entry
from .widgets.labels import create_label
from .widgets.frames import create_main_frame, add_main_label_frame, create_frame
from .enums import LabelTexts
from .utils import get_result, resource_path, setup_hotkeys


def on_closing_result_window(root, window):
    root.deiconify()
    window.destroy()


def create_result_window(root, action, **data):
    try:
        key_value, msg_value = get_result(action, **data)
    except InvalidFileExtensionError:
        messagebox.showerror(
            title='Произошла ошибка',
            message='Несуществующее или невалидное имя файла!',
            parent=root
        )
        return
    except ValueError as e:
        messagebox.showerror(
            title='Произошла ошибка',
            message=str(e),
            parent=root
        )
        return

    window = tkinter.Toplevel(root)
    setup_hotkeys(window)
    window.title('Шифр Виженера')
    window.resizable(False, False)
    window.geometry('500x350')
    icon_path = resource_path('src/frontend/static/icon.png')
    icon = tkinter.PhotoImage(file=icon_path)
    window.iconphoto(False, icon)

    frame = create_main_frame(window)

    add_main_label_frame(frame, LabelTexts.Result)

    key_frame = create_frame(frame)
    key_label = create_label(key_frame, LabelTexts.Key)
    key_entry = create_entry(key_frame, need_pack=False)
    key_entry.pack(padx=5, pady=5, expand=True, anchor='w')
    key_entry.insert(0, key_value)

    message_frame = create_frame(frame)
    message_frame.pack_configure(fill='both')
    message_label = create_label(message_frame, LabelTexts.Message)
    message_text = ScrolledText(message_frame)
    message_text.pack(padx=5, pady=5, fill='x', expand=True)
    message_text.insert(tkinter.INSERT, msg_value)

    root.withdraw()
    window.protocol('WM_DELETE_WINDOW',
                    lambda: on_closing_result_window(root, window))
