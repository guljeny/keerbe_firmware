import displayio
import time
import terminalio
from adafruit_display_text.label import Label
from controllers.keyboardController import keyboard_controller
from controllers.displayController import displayController
from modules.centered_text import centered_text
from utils import clear_display_group
from constants import LAYOUT_CONFIG, DISPLAY_COLOR, DISPLAY_WIDTH, DEFAULT_LAYOUT_KEY

delay_beetween_spm_groups = 1.3

class DisplayInfo():
    def __init__(self):
        self.pressed_keys_count = 0
        self.active_layout = DEFAULT_LAYOUT_KEY
        self.main_layer = displayio.Group()
        self.symbols_typed = 0
        self.start_spm_group = time.monotonic()
        self.last_symbol_typed = 0
        self.first_line_text = Label(terminalio.FONT, text="xxx", color=DISPLAY_COLOR, x=0, y=6)
        self.second_line_text = Label(terminalio.FONT, text="xxx", color=DISPLAY_COLOR, x=0, y=24)
        self.main_layer.append(self.first_line_text)
        self.main_layer.append(self.second_line_text)

        keyboard_controller.subscribe(self.__handle_key_press)
        self.__show_keyboard_stats()

    def __handle_key_press(self, key_name, key_value):
        if key_value:
            self.pressed_keys_count += 1
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
        elif key_value and self.active_layout == DEFAULT_LAYOUT_KEY:
            self.__show_keyboard_stats()

    def __show_keyboard_stats(self):
        type_time_in_minutes = int((time.monotonic() - self.start_spm_group) / 60 * 1000) / 1000
        spm = int(self.symbols_typed / type_time_in_minutes) if type_time_in_minutes else 1
        self.first_line_text.text = "pk: " + str(self.pressed_keys_count)
        self.second_line_text.text = "SPM: " + str(spm)
        self.__update_text_line_position()

    def __show_layer_name(self):
        self.first_line_text.text = "Layer:"
        self.second_line_text.text = self.active_layout
        self.__update_text_line_position()

    def __update_text_line_position(self):
        self.first_line_text.x = int((DISPLAY_WIDTH - len(self.first_line_text.text) * 6) / 2)
        self.second_line_text.x = int((DISPLAY_WIDTH - len(self.second_line_text.text) * 6) / 2)

    def show(self):
        displayController.show(self.main_layer)

display_info = DisplayInfo()
