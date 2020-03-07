from pynput.keyboard import Key, KeyCode, Controller
import pyperclip
import time

current_pressed_key = None

all_pressed_key = set()

def key_string_value(key):
    key = str(KeyCode.from_char(key))
    key = key.replace('Key.', '').replace('"','')
    key = eval(key)
    print("Key_value : {}".format(key))
    return key

def add_key(key):
    global all_pressed_key
    all_pressed_key.add(key)

def remove_key(key):
    global all_pressed_key
    all_pressed_key.remove(key)

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
    # print(all_pressed_key)
    if frozenset(all_pressed_key) == key_combos:
        print("do action")
        print(key_combos)
        print(all_pressed_key)
        return True

    return False
