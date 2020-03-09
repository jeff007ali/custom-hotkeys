from pynput.keyboard import Key, Listener, KeyCode, Controller
from utilities import *


class CustomHotkey:
    def __init__(self, keycombos, keywords):
        self.keycombos = keycombos
        self.keywords = keywords
        
    def on_press(self, key):
        key = key_string_value(key)
        print("on_press : {}".format(key))
        add_key(key)
        # recently_text = update_recent_text(key)
        global recently_typed_text
        recently_typed_text = recently_typed_text + key

        for combo in self.keycombos.values():
            if is_combo_matched(combo):
                combo.run()
        
        for keyword in self.keywords.values():
            # print("keyword scan")
            print("final trigger string : {}".format(keyword.final_trigger_string))
            print("Recently updated text : {}".format(recently_typed_text))
            if keyword.final_trigger_string in recently_typed_text:
                recently_typed_text = ''
                keyword.run()

    def on_release(self, key):
        key = key_string_value(key)
        print("on_release : {}".format(key))
        remove_key(key)
        if key == 'esc':
            return False

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


class KeyCombo:
    def __init__(self, key_list, function, *args, **kwargs):
        self.key_list = frozenset([x.lower() for x in key_list])
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def run(self):
        self.function(*self.args, **self.kwargs)


class KeyWord:
    def __init__(self, trigger_string, replacement_string, *args, **kwargs):
        self.trigger_string = trigger_string
        self.final_trigger_string = ''.join(['space' if x == ' ' else x for x in trigger_string])
        # print("final trigger string : {}".format(self.final_trigger_string))
        self.replacement_string = replacement_string
        self.args = args
        print(args)
        self.kwargs = kwargs
    def run(self):
        replace_keyword(self.trigger_string, self.replacement_string)

