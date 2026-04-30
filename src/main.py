import tkinter

from .frontend.app import App


def main():
    root = tkinter.Tk()
    app = App(root)
    app.root.mainloop()
