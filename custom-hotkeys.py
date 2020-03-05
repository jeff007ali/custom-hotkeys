from pynput.keyboard import Key, Controller, KeyCode, Listener
import pyperclip
import time

def copy_text():
    print('copy')
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

key_combos_with_functions = {
    frozenset([Key.alt, Key.shift, KeyCode(char='U')]): convert_to_uppercase,
    frozenset([Key.alt, KeyCode(char='l')]): convert_to_lowercase,
}

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    print("on_press: {}".format(pressed_keys))
    # print(key_combos_with_functions)
    if frozenset(pressed_keys) in key_combos_with_functions:
        # print("Run things")
        print("In if : {}".format(pressed_keys))
        # print(key_combos_with_functions)
        key_combos_with_functions[frozenset(pressed_keys)]()

def on_release(key):
    print("on_release: {}".format(pressed_keys))
    pressed_keys.remove(key)
    
    # print("on_release: {}".format(pressed_keys))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
