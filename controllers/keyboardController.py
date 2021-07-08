from utils import compare_arrays
from constants import DEFAULT_LAYOUT_KEY, LAYOUT_CONFIG, KEY_MAP

class KeyboardController():
    def __init__(self, layout, key_map = []):
        self.__subscribers = []
        self.__pressed_keys = []
        self.__media_key_pressed = None
        self.layout = layout
        self.key_map = key_map

    def __get_combination (self):
        for key_group in self.key_map:
            if compare_arrays(key_group.get('combination'), self.__pressed_keys):
                return key_group.get('command')
        return None

    def __send_key (self, key_name, key_value):
        for fn, key in self.__subscribers:
            if not key or key == key_name:
                fn(key_name, key_value)

    def handle_key (self, key_value, row, column):
        key_name = self.layout[row][column]
        # print(self.layout, key_name, key_value, row, column)
        if key_value and key_name not in self.__pressed_keys:
            self.__pressed_keys.append(key_name)
            key_name = self.__get_combination() or key_name
            self.__send_key(key_name, key_value)
        elif not key_value and key_name in self.__pressed_keys:
            key_in_combination = self.__get_combination()
            self.__pressed_keys.remove(key_name)
            self.__send_key(key_name, key_value)
            if key_in_combination:
                self.__send_key(key_in_combination, key_value)

    def subscribe (self, callback, key = None):
        self.__subscribers.append((callback, key))

    def unsubscribe (self, callback, key = None):
        self.__subscribers.remove((callback, key))

    def set_layout(self, layout):
        self.layout = layout

keyboard_controller = KeyboardController(LAYOUT_CONFIG[DEFAULT_LAYOUT_KEY], KEY_MAP)
