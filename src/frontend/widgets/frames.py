import tkinter
from tkinter import ttk

from ..utils import select_file, destroy_child_by_name
from ..enums import LabelTexts, ButtonTexts


LABEL_WIDTH = 12


def add_main_label_frame(parent, text):
    frame = _create_frame(parent)
    label = _create_label(frame, text, False, padding=10)
    label['width'] = ''
    label.pack()


def add_enter_key_frame(parent):
    frame = _create_frame(parent)
    label = _create_label(frame, LabelTexts.Key)
    entry = _create_entry(frame)


def add_enter_msg_frame(parent):
    destroy_child_by_name(parent, 'enter_file_frame')

    frame = _create_frame(parent, name='enter_msg_frame')
    label = _create_label(frame, LabelTexts.Message)
    entry = _create_entry(frame)


def add_enter_file_frame(parent):
    destroy_child_by_name(parent, 'enter_msg_frame')

    frame = _create_frame(parent, name='enter_file_frame')
    label = _create_label(frame, LabelTexts.File)

    browse_btn = ttk.Button(frame, text=ButtonTexts.ChooseFile, command=lambda: select_file(entry))
    browse_btn.pack(side='right', padx=5, pady=5)

    entry = _create_entry(frame)


def add_choose_msg_way_frame(parent):
    frame = _create_frame(parent)

    label = _create_label(frame, LabelTexts.MessageWay)
    label['width'] = ''

    radio_val = tkinter.IntVar()

    radio1 = ttk.Radiobutton(frame, text='Файл (.txt)', variable=radio_val, value=1,
                             command=lambda: add_enter_file_frame(parent))
    radio1.pack(side='right', padx=10, pady=5)

    radio2 = ttk.Radiobutton(frame, text='Текст', variable=radio_val, value=2,
                             command=lambda: add_enter_msg_frame(parent))
    radio2.pack(side='right')


#region Widget creators

def create_main_frame(root):
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)
    return frame


def _create_frame(parent, need_pack: bool = True, **options):
    frame = ttk.Frame(parent, **options)
    if need_pack:
        frame.pack(fill='x')
    return frame


def _create_label(parent, text, need_pack: bool = True, **options):
    label = ttk.Label(parent, width=LABEL_WIDTH, text=text, **options)
    if need_pack:
        label.pack(side='left', padx=5)
    return label


def _create_entry(parent, need_pack: bool = True, **options):
    entry = ttk.Entry(parent, **options)
    if need_pack:
        entry.pack(side='right', padx=5, pady=5, fill='x', expand=True)
    return entry

#endregion
