import tkinter

from src.frontend.app import App


def main():
    root = tkinter.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == '__main__':
    main()
