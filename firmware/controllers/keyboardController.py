from utils import compare_arrays
from constants import DEFAULT_LAYOUT_KEY
from config import LAYOUT_CONFIG

class KeyboardController():
    def __init__(self, layout):
        self.__subscribers = []
        self.__pressed_keys = []
        self.__media_key_pressed = None
        self.layout = layout

    def __send_key (self, key_name, key_value):
        for fn, key in self.__subscribers:
            if not key or key == key_name:
                fn(key_name, key_value)

    def handle_key (self, key_value, row, column):
        try:
            key_name = self.layout[row][column]
        except IndexError:
            return

        if not key_name:
            return

        if key_value and key_name not in self.__pressed_keys:
            self.__pressed_keys.append(key_name)
            self.__send_key(key_name, key_value)
        elif not key_value and key_name in self.__pressed_keys:
            self.__pressed_keys.remove(key_name)
            self.__send_key(key_name, key_value)

    def subscribe (self, callback, key = None):
        self.__subscribers.append((callback, key))

    def unsubscribe (self, callback, key = None):
        self.__subscribers.remove((callback, key))

    def set_layout(self, layout):
        self.layout = layout

keyboard_controller = KeyboardController(LAYOUT_CONFIG[DEFAULT_LAYOUT_KEY])
