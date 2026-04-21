import tkinter

from .enums import LabelTexts, ButtonTexts
from .widgets.buttons import (add_return_button,
                              add_get_result_button,
                              add_main_menu_button)
from .widgets.frames import (create_main_frame,
                             create_frame,
                             add_main_label_frame,
                             add_enter_key_frame,
                             add_choose_msg_way_frame)


def create_main_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.MainWindowDescription)
    add_main_label_frame(frame, LabelTexts.MainWindowChooseAction)

    add_main_menu_button(
        root, frame, ButtonTexts.EnterEncryptWindow, WINDOW_CREATORS['encrypt'])
    add_main_menu_button(
        root, frame, ButtonTexts.EnterDecryptWindow, WINDOW_CREATORS['decrypt'])
    add_main_menu_button(
        root, frame, ButtonTexts.EnterBreakWindow, WINDOW_CREATORS['break'])


def create_encrypt_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.EncryptWindow)
    add_enter_key_frame(frame)
    add_choose_msg_way_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(buttons_frame, action='encrypt')
    add_return_button(root, buttons_frame, create_main_window)


def create_decrypt_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.DecryptWindow)
    add_enter_key_frame(frame)
    add_choose_msg_way_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(buttons_frame, action='decrypt')
    add_return_button(root, buttons_frame, create_main_window)


def create_breaker_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.BreakWindow)
    add_choose_msg_way_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(buttons_frame, action='break')
    add_return_button(root, buttons_frame, create_main_window)


WINDOW_CREATORS = {
    'encrypt': create_encrypt_window,
    'decrypt': create_decrypt_window,
    'break': create_breaker_window,
    'main': create_main_window
}
