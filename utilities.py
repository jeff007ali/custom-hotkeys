from pynput.keyboard import Key, KeyCode, Controller
import pyperclip
import time

recently_typed_text = ''

currently_pressed_keys = set()

def key_string_value(key):
    key = str(KeyCode.from_char(key))
    key = key.replace('Key.', '').replace('"','')
    key = eval(key)
    key = key.lower()
    if key == '<65511>':
        key = 'alt'
    elif key == '<65512>':
        key = 'alt_r'
    # print("Key_value : {}".format(key))
    return key

def add_key(key):
    global currently_pressed_keys
    currently_pressed_keys.add(key)

def remove_key(key):
    global currently_pressed_keys
    currently_pressed_keys.remove(key)

def update_recent_text(key):
    global recently_typed_text
    if key in ['ctrl', 'ctrl_r', 'alt', 'alt_r']:
        pass
    recently_typed_text = recently_typed_text + key

def delete_text(string):
    keyboard = Controller()
    for _ in string:
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.05)

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

def replace_keyword(keyword, string):
    pyperclip.copy(string)
    delete_text(keyword)
    paste_text()

def is_combo_matched(combo):
    key_combos = combo.key_list
    # print(key_combos)
    # print(currently_pressed_keys)
    if frozenset(currently_pressed_keys) == key_combos:
        print("do action")
        print(key_combos)
        print(currently_pressed_keys)
        return True

    return False
