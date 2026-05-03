import tkinter

from .utils import resource_path, setup_hotkeys
from .page_creators import create_main_page


class App:
    def __init__(self, root):
        self.root = self._config(root)

    @staticmethod
    def _config(root):
        setup_hotkeys(root)

        root.title('Шифр Виженера')

        root.resizable(False, False)
        root.geometry('400x300')

        icon_path = resource_path('src/frontend/static/icon.png')
        icon = tkinter.PhotoImage(file=icon_path)
        root.iconphoto(False, icon)

        create_main_page(root)
        return root
