import tkinter
from tkinter import ttk

from .buttons import create_browse_button
from .labels import create_label
from .entries import create_entry
from ..enums import LabelTexts, RadioButtonTexts
from ..constants import RADIO_MESSAGE_WAY_VALUES, RADIO_LANGUAGE_VALUES


def add_main_label_frame(parent, text):
    frame = create_frame(parent)
    label = create_label(frame, text, False, padding=10)
    label['width'] = ''
    label.pack()


def add_enter_key_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.Key)
    entry = create_entry(frame)
    return entry


def add_enter_msg_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.Message)
    entry = create_entry(frame)
    return entry


def add_enter_file_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.File)
    entry = create_entry(frame)
    browse_btn = create_browse_button(frame, entry)
    return entry


def add_choose_msg_way_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.MessageWay, width=25)

    radio_val = tkinter.StringVar()

    radio1 = ttk.Radiobutton(
        frame, text=RadioButtonTexts.File, variable=radio_val, value=RADIO_MESSAGE_WAY_VALUES[1])
    radio1.pack(side='left', padx=10, pady=5)

    radio2 = ttk.Radiobutton(
        frame, text=RadioButtonTexts.Text, variable=radio_val, value=RADIO_MESSAGE_WAY_VALUES[0])
    radio2.pack(side='left')

    return radio_val


def add_choose_lang_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.Language, width=25)

    radio_val = tkinter.StringVar()

    radio1 = ttk.Radiobutton(
        frame, text=RadioButtonTexts.LanguageRU, variable=radio_val, value=RADIO_LANGUAGE_VALUES[0])
    radio1.pack(side='left', padx=10, pady=5)

    radio2 = ttk.Radiobutton(
        frame, text=RadioButtonTexts.LanguageEN, variable=radio_val, value=RADIO_LANGUAGE_VALUES[1])
    radio2.pack(side='left')

    return radio_val


def create_main_frame(root):
    """
    Create the main frame for the window
    Args:
        root: Window
    Returns:
        Packed frame that fills window
    """
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)
    return frame


def create_frame(parent, need_pack: bool = True, **options):
    frame = ttk.Frame(parent, **options)
    if need_pack:
        frame.pack(fill='x')
    return frame
