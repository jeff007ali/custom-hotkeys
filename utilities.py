from pynput.keyboard import Key, KeyCode, Controller
import pyperclip
import time

recently_typed_text = ''

currently_pressed_keys = set()

kb = Controller()

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
    recently_typed_text = recently_typed_text + key
    print("Utility, Recently updated text : {}".format(recently_typed_text))
    return recently_typed_text

def get_recent_text(keyword):
    print("in recent text")
    select_text(keyword)
    copy_text()
    print(read_clipboard_data())
    return read_clipboard_data()

def select_text(text):
    print("in select text")
    # kb = Controller()
    kb.press(Key.shift)
    for _ in text:
        kb.press(Key.left)
        kb.release(Key.left)
    kb.release(Key.shift)


def delete_text(string):
    # kb = Controller()
    for _ in string:
        kb.press(Key.backspace)
        kb.release(Key.backspace)
        time.sleep(0.05)

def copy_text():
    # print('copy')
    # kb = Controller()
    kb.press(Key.ctrl_l)
    kb.press('c')
    kb.release('c')
    kb.release(Key.ctrl_l)
    time.sleep(0.1)

def paste_text():
    # print('paste')
    # kb = Controller()
    kb.press(Key.ctrl_l)
    kb.press('v')
    kb.release('v')
    kb.release(Key.ctrl_l)

def replace_keyword(keyword, text):
    write_clipboard_data(text)
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

def read_clipboard_data():
    return pyperclip.paste()

def write_clipboard_data(data):
    pyperclip.copy(data)

def clear_clipboard_data():
    pyperclip.copy('')

def before_conversion():
    # print("before conversation")
    clear_clipboard_data()
    copy_text()
    data = read_clipboard_data()
    return data

def after_conversion(data):
    # print("after conversation")
    write_clipboard_data(data)
    paste_text()