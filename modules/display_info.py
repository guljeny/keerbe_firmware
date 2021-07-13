import displayio
import time
import terminalio
from adafruit_display_text.label import Label
from controllers.keyboardController import keyboard_controller
from controllers.displayController import displayController
from controllers.storageController import storage_controller
from modules.centered_text import centered_text
from utils import clear_display_group, number_to_array, bytearray_to_number_array
from constants import LAYOUT_CONFIG, DISPLAY_COLOR, DISPLAY_WIDTH, DEFAULT_LAYOUT_KEY, SAVED_KEY_PRESSED_FIRST_BIT, SAVED_KEY_PRESSED_LENGTH

delay_beetween_spm_groups = 1.3

class DisplayInfo():
    def __init__(self):
        self.pressed_counter_list = [0,0,0,0,0,0,0,0,0,0,0,0]

        self.active_layout = DEFAULT_LAYOUT_KEY
        self.root_layer = displayio.Group()
        self.counter_layer = displayio.Group()

        self.symbols_typed = 0
        self.start_spm_group = time.monotonic()
        self.last_symbol_typed = 0
        self.first_line_text = Label(terminalio.FONT, text="xxx", color=DISPLAY_COLOR, x=0, y=6)
        self.second_line_text = Label(terminalio.FONT, text="xxx", color=DISPLAY_COLOR, x=0, y=24)
        
        self.counter_numbers_layers = []
        offset = 0
        for index, num in enumerate(self.pressed_counter_list, start=0):
            if index and not index % 3:
                offset += 6
            label = Label(terminalio.FONT, text=str(num), color=DISPLAY_COLOR, x=index*6 + offset, y=6)
            self.counter_numbers_layers.append(label)
            self.counter_layer.append(label)

        self.counter_layer.x = 20 

        self.root_layer.append(self.first_line_text)
        self.root_layer.append(self.second_line_text)
        self.root_layer.append(self.counter_layer)

        keyboard_controller.subscribe(self.__handle_key_press)
        self.__show_keyboard_stats()
        storage_controller.read(self.__set_pressed_keys, SAVED_KEY_PRESSED_LENGTH, SAVED_KEY_PRESSED_FIRST_BIT)

    def __set_pressed_keys (self, bytearray_of_pressed_keys):
        self.pressed_counter_list = bytearray_to_number_array(bytearray_of_pressed_keys)
        self.__update_keyboard_stats()

    def __increment_pressed_keys_count(self, index = 0):
        position = len(self.pressed_counter_list) - index - 1
        if position < 0:
            return
        if self.pressed_counter_list[position] == 9:
            self.pressed_counter_list[position] = 0
            self.__increment_pressed_keys_count(index + 1)
        else:
            self.pressed_counter_list[position] += 1


    def __handle_key_press(self, key_name, key_value):
        if key_value:
            self.__increment_pressed_keys_count()

            storage_controller.write(self.pressed_counter_list, SAVED_KEY_PRESSED_FIRST_BIT)
            now = time.monotonic()
            if now - self.last_symbol_typed > delay_beetween_spm_groups:
                self.start_spm_group = now
                self.symbols_typed = 0
            self.symbols_typed += 1
            self.last_symbol_typed = now

        if key_name in LAYOUT_CONFIG:
            if key_value:
                self.active_layout = key_name
                self.__show_layer_name()
            else:
                self.active_layout = DEFAULT_LAYOUT_KEY
                self.__show_keyboard_stats()
                self.__update_keyboard_stats()
        elif key_value and self.active_layout == DEFAULT_LAYOUT_KEY:
            self.__update_keyboard_stats()

    def __update_keyboard_stats(self):
        type_time_in_minutes = int((time.monotonic() - self.start_spm_group) / 60 * 1000) / 1000
        spm = int(self.symbols_typed / type_time_in_minutes) if type_time_in_minutes else 1
        self.second_line_text.text = "SPM: " + str(spm)

        for index, num in enumerate(self.pressed_counter_list, start=0):
            if self.counter_numbers_layers[index].text != str(num):
                self.counter_numbers_layers[index].text = str(num)

    def __show_keyboard_stats(self):
        self.first_line_text.text = "   ,   ,   ,   "
        self.second_line_text.text = "SPM: 0"
        self.counter_layer.hidden = False
                
        self.__update_text_line_position()

    def __show_layer_name(self):
        self.counter_layer.hidden = True
        self.first_line_text.text = "Layer:"
        self.second_line_text.text = self.active_layout
        self.__update_text_line_position()

    def __update_text_line_position(self):
        self.first_line_text.x = int((DISPLAY_WIDTH - len(self.first_line_text.text) * 6) / 2)
        self.second_line_text.x = int((DISPLAY_WIDTH - len(self.second_line_text.text) * 6) / 2)

    def show(self):
        displayController.show(self.root_layer)

display_info = DisplayInfo()
