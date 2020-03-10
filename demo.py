from custom_hotkey import CustomHotkey, KeyCombo, KeyWord
from utilities import *
from pynput.keyboard import Key, Controller, KeyCode, Listener
import pyperclip
import time

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
    

keycombos = {
    'lowercase': KeyCombo(['alt', 'shift', 'L'], lowercase),
    'uppercase': KeyCombo(['alt', 'u'], uppercase)
#     frozenset([Key.alt, Key.shift, KeyCode(char='U')]): convert_to_uppercase,
#     frozenset([Key.alt, KeyCode(char='l')]): convert_to_lowercase,
}

keywords = {
    'signature': KeyWord('-jeff', 'Regards,\nJafar Ali')
}

custom_hotkey = CustomHotkey(keycombos=keycombos, keywords=keywords)
custom_hotkey.run()
