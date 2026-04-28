import tkinter

from .widgets.labels import create_label
from .widgets.frames import create_main_frame, add_main_label_frame, create_frame
from .enums import LabelTexts
from .utils import get_result


def create_result_window(root, action, **data):
    window = tkinter.Toplevel(root)
    window.title('Шифр Виженера')
    window.resizable(False, False)
    window.geometry('600x500')
    icon = tkinter.PhotoImage(file='src/frontend/static/icon.png')
    window.iconphoto(False, icon)

    frame = create_main_frame(window)

    add_main_label_frame(frame, LabelTexts.Result)

    result = get_result(action, **data)

    key_frame = create_frame(frame)
    key_label = create_label(key_frame, LabelTexts.Key)

    message_frame = create_frame(frame)
    message_label = create_label(message_frame, LabelTexts.Message)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
