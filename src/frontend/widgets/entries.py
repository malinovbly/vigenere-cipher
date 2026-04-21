from tkinter import ttk


def create_entry(parent, need_pack: bool = True, **options):
    entry = ttk.Entry(parent, **options)
    if need_pack:
        entry.pack(padx=5, pady=5, fill='x', expand=True)
    return entry
