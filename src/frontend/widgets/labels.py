from tkinter import ttk


def create_label(
        parent, text, need_pack: bool = True, width = 12, **options):
    label = ttk.Label(parent, width=width, text=text, **options)
    if need_pack:
        label.pack(side='left', anchor='n', padx=5, pady=5)
    return label
