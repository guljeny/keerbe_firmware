import displayio
import time
import terminalio
from adafruit_display_text.label import Label
from controllers.keyboardController import keyboard_controller
from controllers.displayController import displayController
from modules.centered_text import centered_text
from utils import clear_display_group
from constants import LAYOUT_CONFIG, DISPLAY_COLOR, DISPLAY_WIDTH
from modules.event_loop import event_loop

DELAY_TO_REDRAW = 0.5

class DisplayInfo():
    def __init__(self):
        self.pressed_keys_count = 0
        self.main_layer = displayio.Group()
        # self.first_line_layer = displayio.Group()
        # self.second_line_layer = displayio.Group()

        # first_line_text = Label(terminalio.FONT, text=text, color=DISPLAY_COLOR, x=int((DISPLAY_WIDTH - len(text) * 6) / 2), y=6)
        self.last_update_time = 0
        self.text_for_first_line = "xxx"
        self.text_for_second_line = "xxx"
        self.first_line_text = Label(terminalio.FONT, text=self.text_for_first_line, color=DISPLAY_COLOR, x=0, y=6)
        self.second_line_text = Label(terminalio.FONT, text=self.text_for_second_line, color=DISPLAY_COLOR, x=0, y=24)
        # self.pressed_keys_layer = displayio.Group()
        # self.write_speed_layer = displayio.Group()
        self.main_layer.append(self.first_line_text)
        self.main_layer.append(self.second_line_text)

        keyboard_controller.subscribe(self.__handle_key_press)
        self.__show_info()
        event_loop.append(self.__loop)

    def __handle_key_press(self, key_name, key_value):
        if key_value:
            self.pressed_keys_count += 1

        if key_name in LAYOUT_CONFIG and key_value:
            self.__show_layer_name(key_name)
        else:
            self.__show_info()

    def __show_info(self):
        self.text_for_first_line = "pk: " + str(self.pressed_keys_count)
        self.text_for_second_line = "SPM: " + str(123)

        # self.__update_text_line(self.first_line_text, first_line_text)
        # self.__update_text_line(self.second_line_text, second_line_text)

    def __show_layer_name(self, layer_name):
        self.text_for_first_line = "Layer:"
        self.text_for_second_line = layer_name

        # self.__update_text_line(self.first_line_text, first_line_text)
        # self.__update_text_line(self.second_line_text, second_line_text)

    def __update_text_line(self, line, text):
        if text != line.text:
            line._reset_text(text)
            line.x = int((DISPLAY_WIDTH - len(text) * 6) / 2)

    def __loop(self):
        now = time.monotonic()
        if now > self.last_update_time + DELAY_TO_REDRAW:
            self.last_update_time = now
            self.__update_text_line(self.first_line_text, self.text_for_first_line)
            self.__update_text_line(self.second_line_text, self.text_for_second_line)

    def show(self):
        displayController.show(self.main_layer)

display_info = DisplayInfo()
