import tkinter
from tkinter import ttk

from .utils import resource_path
from .page_creators import create_main_page


class App:
    def __init__(self, root):
        root.bind("<Control-KeyPress>", self._keypress)
        self.root = self._config(root)

    @staticmethod
    def _config(root):
        root.title('Шифр Виженера')

        root.resizable(False, False)
        root.geometry('400x300')

        icon_path = resource_path('src/frontend/static/icon.png')
        icon = tkinter.PhotoImage(file=icon_path)
        root.iconphoto(False, icon)

        create_main_page(root)
        return root

    def _keypress(self, e):
        if e.keycode == 86 and e.keysym != 'v':
            self._cmd_paste()
        elif e.keycode == 67 and e.keysym != 'c':
            self._cmd_copy()
        elif e.keycode == 88 and e.keysym != 'x':
            self._cmd_cut()

    def _cmd_copy(self):
        widget = self.root.focus_get()
        if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
            widget.event_generate("<<Copy>>")

    def _cmd_cut(self):
        widget = self.root.focus_get()
        if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
            widget.event_generate("<<Cut>>")

    def _cmd_paste(self):
        widget = self.root.focus_get()
        if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
            widget.event_generate("<<Paste>>")
