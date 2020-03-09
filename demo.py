from custom_hotkey import CustomHotkey, KeyCombo, KeyWord
from pynput.keyboard import Key, Controller, KeyCode, Listener
import pyperclip
import time

def read_clipboard_data():
    return pyperclip.paste()

def write_clipboard_data(data):
    pyperclip.copy(data)

def clear_clipboard_data():
    pyperclip.copy('')

def copy_text():
    # print('copy')
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.1)

def paste_text():
    # print('paste')
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)

def convert_to_uppercase():
    print("In uppercase function")
    clear_clipboard_data()
    # data = pyperclip.paste()
    # print('data before copy : {}'.format(data))
    copy_text()
    data = read_clipboard_data()
    print('data after copy : {}'.format(data))

    data = data.upper()

    # print('modified data before paste : {}'.format(data))
    write_clipboard_data(data)
    paste_text()
    # print('modified data after paste : {}'.format(data))

def convert_to_lowercase():
    # print("In lowercase function")
    clear_clipboard_data()
    # data = pyperclip.paste()
    # print('data before copy : {}'.format(data))
    copy_text()
    data = read_clipboard_data()
    # print('data after copy : {}'.format(data))

    data = data.lower()

    # print('modified data before paste : {}'.format(data))
    write_clipboard_data(data)
    paste_text()
    # print('modified data after paste : {}'.format(data))


# TODO : Try this out
"""
    from pynput import keyboard

    def on_activate_h():
        print('<ctrl>+<alt>+h pressed')

    def on_activate_i():
        print('<ctrl>+<alt>+i pressed')

    with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+h': on_activate_h,
            '<ctrl>+<alt>+i': on_activate_i}) as h:
        h.join()
"""

keycombos = {
    'lowercase': KeyCombo(['alt', 'shift', 'L'], convert_to_lowercase),
    'uppercase': KeyCombo(['alt', 'u'], convert_to_uppercase)
#     frozenset([Key.alt, Key.shift, KeyCode(char='U')]): convert_to_uppercase,
#     frozenset([Key.alt, KeyCode(char='l')]): convert_to_lowercase,
}

keywords = {
    'signature': KeyWord('-jeff', 'Regards,\nJafar Ali')
}

custom_hotkey = CustomHotkey(keycombos=keycombos, keywords=keywords)
custom_hotkey.run()
