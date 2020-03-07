from pynput.keyboard import Key, Listener, KeyCode
from utilities import *

class CustomHotkey:
    def __init__(self, keycombos, keywords):
        self.keycombos = keycombos
        self.keywords = keywords

    def on_press(self, key):
        key = key_string_value(key)
        add_key(key)

        for combo in self.keycombos.values():
            if is_combo_matched(combo):
                combo.run()

    def on_release(self, key):
        key = key_string_value(key)
        print("on_release : {}".format(key))
        remove_key(key)

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


class KeyCombo:
    def __init__(self, key_list, function, *args, **kwargs):
        self.key_list = frozenset(key_list)
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def run(self):
        self.function(*self.args, **self.kwargs)


class KeyWord:
    def __init__(self, trigger_string, *args, **kwargs):
        self.trigger_string = trigger_string
        self.final_trigger_string = ''.join(['space' if x == ' ' else x for x in trigger_string])
        self.args = args
        self.kwargs = kwargs
    def run(self):
        replace_keyword(self.trigger_string, *self.args, **self.kwargs)

