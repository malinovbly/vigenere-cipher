from .enums import LabelTexts, ButtonTexts
from .widgets.buttons import (add_return_button,
                              add_get_result_button,
                              add_main_menu_button)
from .widgets.frames import (create_main_frame,
                             create_frame,
                             add_main_label_frame,
                             add_enter_key_frame,
                             add_enter_msg_frame,
                             add_enter_file_frame,
                             add_choose_msg_way_frame,
                             add_choose_lang_frame)
from .window_creators import create_result_window


def create_main_page(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.MainWindowDescription)
    add_main_label_frame(frame, LabelTexts.MainWindowChooseAction)

    add_main_menu_button(
        root, frame, ButtonTexts.EnterEncryptWindow, PAGE_CREATORS['encrypt'])
    add_main_menu_button(
        root, frame, ButtonTexts.EnterDecryptWindow, PAGE_CREATORS['decrypt'])
    add_main_menu_button(
        root, frame, ButtonTexts.EnterBreakWindow, PAGE_CREATORS['break'])


def create_encrypt_page(root):
    frame = create_main_frame(root)
    add_main_label_frame(frame, LabelTexts.EncryptWindow)

    key = add_enter_key_frame(frame)
    radio_language = add_choose_lang_frame(frame)
    radio_message_way = add_choose_msg_way_frame(frame)
    message = add_enter_msg_frame(frame)
    file_name = add_enter_file_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(
        root, buttons_frame, 'encrypt', create_result_window,
        key=key, message=message, file_name=file_name,
        radio_message_way=radio_message_way, radio_language=radio_language
    )
    add_return_button(root, buttons_frame, create_main_page)


def create_decrypt_page(root):
    frame = create_main_frame(root)
    add_main_label_frame(frame, LabelTexts.DecryptWindow)

    key = add_enter_key_frame(frame)
    radio_language = add_choose_lang_frame(frame)
    radio_message_way = add_choose_msg_way_frame(frame)
    message = add_enter_msg_frame(frame)
    file_name = add_enter_file_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(
        root, buttons_frame, 'decrypt', create_result_window,
        key=key, message=message, file_name=file_name,
        radio_message_way=radio_message_way, radio_language=radio_language
    )
    add_return_button(root, buttons_frame, create_main_page)


def create_breaker_page(root):
    frame = create_main_frame(root)
    add_main_label_frame(frame, LabelTexts.BreakWindow)

    radio_language = add_choose_lang_frame(frame)
    radio_message_way = add_choose_msg_way_frame(frame)
    message = add_enter_msg_frame(frame)
    file_name = add_enter_file_frame(frame)

    buttons_frame = create_frame(frame)
    buttons_frame.pack_configure(side='bottom')
    add_get_result_button(
        root, buttons_frame, 'break', create_result_window,
        message=message, file_name=file_name,
        radio_message_way=radio_message_way, radio_language=radio_language
    )
    add_return_button(root, buttons_frame, create_main_page)


PAGE_CREATORS = {
    'encrypt': create_encrypt_page,
    'decrypt': create_decrypt_page,
    'break': create_breaker_page,
    'main': create_main_page,
}
