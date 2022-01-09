import displayio
import time
import terminalio
from adafruit_display_text.label import Label
from controllers.displayController import displayController
from controllers.storageController import storage_controller
from utils import clear_display_group, restore_after_save, prepare_to_save
from constants import DISPLAY_COLOR, DISPLAY_WIDTH, DEFAULT_LAYOUT_KEY, SAVED_KEY_PRESSED_FIRST_BIT, SAVED_KEY_PRESSED_LENGTH, DISABLE_DISPLAY_BUTTON
from config import TIME_TO_DISPLAY_SLEEP
from config import LAYOUT_CONFIG
from modules.event_loop import event_loop

delay_beetween_spm_groups = 1.3 # TODO: read it from config

class DisplayInfo():
    def __init__ (self):
        self.is_display_enabled = True
        self.root_layer = displayio.Group()
        self.pressed_keys_comma_layer = Label(terminalio.FONT, text="   ,   ,   ,   ")
        self.pressed_keys_comma_layer.x = 0
        self.pressed_keys_comma_layer.y = 6
        self.spm_layer = Label(terminalio.FONT, text="SPM: 0", color=DISPLAY_COLOR)
        self.spm_layer.x = 0
        self.spm_layer.y = 24

        self.pressed_keys_count_in_array = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.pressed_keys_count_digit_layers = []
        self.pressed_keys_count_layer = displayio.Group()

        self.time_from_start_spm_match = time.monotonic()
        self.last_symbol_typed_time = self.time_from_start_spm_match
        self.symbols_typed_from_start_spm_match = 0

        self.__fill_pressed_keys_count_layer()

        self.pressed_keys_comma_layer.x = 20 
        self.pressed_keys_count_layer.x = 20 
        self.__center_spm_layer()

        self.root_layer.append(self.pressed_keys_count_layer)
        self.root_layer.append(self.pressed_keys_comma_layer)
        self.root_layer.append(self.spm_layer)

        storage_controller.read(self.__set_pressed_keys_from_memory, SAVED_KEY_PRESSED_LENGTH, SAVED_KEY_PRESSED_FIRST_BIT)
        event_loop.append(self.__loop)

    def __loop (self):
        now = time.monotonic()

        if now > self.last_symbol_typed_time + TIME_TO_DISPLAY_SLEEP and displayController.is_awake:
            displayController.sleep()

        if now > self.last_symbol_typed_time + delay_beetween_spm_groups and self.time_from_start_spm_match:
            type_time_in_minutes = int((time.monotonic() - self.time_from_start_spm_match) / 60 * 1000) / 1000
            spm = int(self.symbols_typed_from_start_spm_match / type_time_in_minutes) if type_time_in_minutes else 1
            self.time_from_start_spm_match = 0
            self.symbols_typed_from_start_spm_match = 0
            self.spm_layer.text = "SPM: " + str(spm)
            self.__center_spm_layer()

    def __fill_pressed_keys_count_layer (self):
        offset = 0
        for index, num in enumerate(self.pressed_keys_count_in_array, start=0):
            if index and not index % 3:
                offset += 6
            label = Label(terminalio.FONT, text=str(num), color=DISPLAY_COLOR, x=index*6 + offset, y=6)
            self.pressed_keys_count_digit_layers.append(label)
            self.pressed_keys_count_layer.append(label)

    def __set_pressed_keys_from_memory (self, bytearray_of_pressed_keys):
        self.pressed_keys_count_in_array = restore_after_save(bytearray_of_pressed_keys)
        self.__update_pressed_keys_count_layers()

    def __increment_pressed_keys_count(self, index = 0):
        position = len(self.pressed_keys_count_in_array) - index - 1
        if position < 0:
            return
        if self.pressed_keys_count_in_array[position] == 9:
            self.pressed_keys_count_in_array[position] = 0
            self.__increment_pressed_keys_count(index + 1)
        else:
            self.pressed_keys_count_in_array[position] += 1

    def __calc_spm (self):
        now = time.monotonic()
        if not self.time_from_start_spm_match:
            self.time_from_start_spm_match = now
        self.symbols_typed_from_start_spm_match += 1
        self.last_symbol_typed_time = now

    def __update_pressed_keys_count_layers (self):
        for index, num in enumerate(self.pressed_keys_count_in_array, start=0):
            if self.pressed_keys_count_digit_layers[index].text != str(num):
                self.pressed_keys_count_digit_layers[index].text = str(num)

    def __center_spm_layer (self):
        self.spm_layer.x = int((DISPLAY_WIDTH - len(self.spm_layer.text) * 6) / 2)

    def show (self):
        displayController.show(self.root_layer)

    def handle_key_press (self, key_name, key_value):
        if key_value:
            if not displayController.is_awake and self.is_display_enabled:
                displayController.wake()

            if key_name == DISABLE_DISPLAY_BUTTON:
                self.is_display_enabled = not self.is_display_enabled
                displayController.wake() if self.is_display_enabled else displayController.sleep()

            self.__increment_pressed_keys_count()
            self.__calc_spm()
            storage_controller.write(prepare_to_save(self.pressed_keys_count_in_array), SAVED_KEY_PRESSED_FIRST_BIT)
            self.__update_pressed_keys_count_layers()
