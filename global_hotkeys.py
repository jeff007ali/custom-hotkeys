from pynput import keyboard
from pynput.keyboard import Controller, Key
import pyperclip
import time
import random

kb = Controller()

def read_clipboard_data():
    return pyperclip.paste()

def write_clipboard_data(data):
    pyperclip.copy(data)

def clear_clipboard_data():
    pyperclip.copy('')

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


def uppercase():
    data = before_conversion()
    data = data.upper()
    print(data)
    after_conversion(data)

def lowercase():
    data = before_conversion()
    data = data.lower()
    print(data)
    after_conversion(data)

def flip():
    data = before_conversion()
    data = ''.join([x.upper() if x == x.lower() else x.lower() for x in data])
    print(data)
    after_conversion(data)

def capitalize():
    data = before_conversion()
    data = data.capitalize()
    print(data)
    after_conversion(data)

def capitalize_every_word():
    data = before_conversion()
    print(data)
    data = data.title()
    print(data)
    after_conversion(data)

def alternate():
    data = before_conversion()
    data = [x for x in data]
    for i, c in enumerate(data):
        data[i] = c.upper() if i % 2 == 0 else c.lower()
    data = ''.join(data)
    print(data)
    after_conversion(data)

def spongebob():
    data = before_conversion()
    data = [x for x in data]
    for i, c in enumerate(data):
        data[i] = random.choice([c.upper(), c.lower()])
    data = ''.join(data)
    print(data)
    after_conversion(data)

def snake_case():
    data = before_conversion()
    data = data.split()
    data = [x.lower() for x in data]
    data = '_'.join(data)
    print(data)
    after_conversion(data)

def reverse():
    data = before_conversion()
    data = data[::-1]
    print(data)
    after_conversion(data)

def compute():
    data = before_conversion()
    try:	
        data = eval(data)	
    except:
        data = data
    print(data)
    after_conversion(data)

# sometimes gives weird behaviour
with keyboard.GlobalHotKeys({
        '<alt>+1': uppercase,
        '<alt>+2': lowercase,
        '<alt>+3': flip,
        '<alt>+4': capitalize,
        '<alt>+5': capitalize_every_word,
        '<alt>+6': alternate,
        '<alt>+7': spongebob,
        '<alt>+8': snake_case,
        '<alt>+9': reverse,
        '<alt>+0': compute
        }) as h:
    h.join()