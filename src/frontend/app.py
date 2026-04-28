import tkinter

from .page_creators import create_main_page


def create_app() -> tkinter.Tk:
    root = tkinter.Tk()
    root.title('Шифр Виженера')

    root.resizable(False, False)
    root.geometry('400x300')

    icon = tkinter.PhotoImage(file='src/frontend/static/icon.png')
    # icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)

    return root


def main():
    root = create_app()
    create_main_page(root)
    root.mainloop()


if __name__ == '__main__':


    main()
