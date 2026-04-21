import tkinter
from tkinter import ttk

from .buttons import create_browse_button
from .labels import create_label
from .entries import create_entry
from ..utils import destroy_child_by_name
from ..enums import LabelTexts, RadioButtonTexts


def add_main_label_frame(parent, text):
    frame = create_frame(parent)
    label = create_label(frame, text, False, padding=10)
    label['width'] = ''
    label.pack()


def add_enter_key_frame(parent):
    frame = create_frame(parent)
    label = create_label(frame, LabelTexts.Key)
    entry = create_entry(frame)


def add_enter_msg_frame(parent):
    destroy_child_by_name(parent, 'enter_file_frame')
    frame = create_frame(parent, name='enter_msg_frame')

    label = create_label(frame, LabelTexts.Message)
    entry = create_entry(frame)


def add_enter_file_frame(parent):
    destroy_child_by_name(parent, 'enter_msg_frame')
    frame = create_frame(parent, name='enter_file_frame')

    label = create_label(frame, LabelTexts.File)
    entry = create_entry(frame)
    browse_btn = create_browse_button(frame, entry)


def add_choose_msg_way_frame(parent):
    frame = create_frame(parent)

    label = create_label(frame, LabelTexts.MessageWay, width='')

    radio_val = tkinter.IntVar()

    radio1 = ttk.Radiobutton(frame, text=RadioButtonTexts.File, variable=radio_val, value=1,
                             command=lambda: add_enter_file_frame(parent))
    radio1.pack(side='left', padx=10, pady=5)

    radio2 = ttk.Radiobutton(frame, text=RadioButtonTexts.Text, variable=radio_val, value=2,
                             command=lambda: add_enter_msg_frame(parent))
    radio2.pack(side='left')


#region Local utils

def create_main_frame(root):
    """
    Create the main frame for the window
    Args:
        root (tkinter.Tk): The root window (app)
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

#endregion
