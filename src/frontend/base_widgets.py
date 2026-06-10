import tkinter
from math import floor
from tkinter import ttk


def create_frame(parent, need_pack=True, **options):
    frame = ttk.Frame(parent, **options)
    if need_pack:
        frame.pack(fill='x')
    return frame


def create_label(parent, text, need_pack=True, width=12, **options):
    label = ttk.Label(parent, width=width, text=text, **options)
    if need_pack:
        label.pack(side='left', anchor='n', padx=5, pady=5)
    return label


def create_entry(parent, need_pack=True, **options):
    entry = ttk.Entry(parent, **options)
    if need_pack:
        entry.pack(padx=15, pady=5, fill='x', expand=True)
    return entry


def create_text(parent, cnt_per_frame=1, need_pack=True, **options):
    height = floor(26 / cnt_per_frame)
    text = tkinter.Text(parent, height=height, **options)
    if need_pack:
        text.pack(padx=15, pady=5, fill='x', expand=True)
    return text
