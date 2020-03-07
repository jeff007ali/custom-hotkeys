from custom_hotkey import CustomHotkey, KeyCombo, KeyWord
from pynput.keyboard import Key, Controller, KeyCode, Listener
import pyperclip
import time

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
    data = pyperclip.copy('')
    # data = pyperclip.paste()
    # print('data before copy : {}'.format(data))
    copy_text()
    data = pyperclip.paste()
    print('data after copy : {}'.format(data))

    data = data.upper()

    # print('modified data before paste : {}'.format(data))
    pyperclip.copy(data)
    paste_text()
    # print('modified data after paste : {}'.format(data))

def convert_to_lowercase():
    # print("In lowercase function")
    data = pyperclip.copy('')
    # data = pyperclip.paste()
    # print('data before copy : {}'.format(data))
    copy_text()
    data = pyperclip.paste()
    # print('data after copy : {}'.format(data))

    data = data.lower()

    # print('modified data before paste : {}'.format(data))
    pyperclip.copy(data)
    paste_text()
    # print('modified data after paste : {}'.format(data))



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
