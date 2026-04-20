import tkinter

from .window_creators import create_main_window


def create_app() -> tkinter.Tk:
    root = tkinter.Tk()
    root.title('Шифр Виженера')

    root.resizable(False, False)
    root.geometry('400x250')

    icon = tkinter.PhotoImage(file='src/frontend/icon.png')
    # icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)

    return root


def main():
    root = create_app()
    create_main_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
