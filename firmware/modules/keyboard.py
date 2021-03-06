import usb_hid
import time
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard as KeyboardControl
from adafruit_hid.consumer_control import ConsumerControl
from constants import DEFAULT_LAYOUT_KEY, SHOW_GAME_BUTTON, DISABLE_DISPLAY_BUTTON
from config import GAME_PLAY_BUTTON, LAYOUT_CONFIG, TIME_TO_DISPLAY_SLEEP, KEYBOARD_WITH_DISPLAY
from controllers.displayController import displayController
from modules.flappyDotGame import FlappyDotGame
from modules.display_info import DisplayInfo

keyboard_control = KeyboardControl(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

flappyDotGame = FlappyDotGame()

class Keyboard ():
    def __init__(self):
        self.__media_key_pressed = None
        self.layout = DEFAULT_LAYOUT_KEY
        self.__pressed_keys = []
        if KEYBOARD_WITH_DISPLAY:
            self.display_info = DisplayInfo()
            self.display_info.show()
    
    def handle_key (self, key_value, row, column):
        try:
            key_name = LAYOUT_CONFIG[self.layout][row][column]
        except IndexError:
            return

        if not key_name:
            return

        # Update display_info if keyboard supports display
        if KEYBOARD_WITH_DISPLAY:
            self.display_info.handle_key_press(key_name, key_value)

            if key_value:
                if flappyDotGame.is_game_enabled:
                    if key_name == GAME_PLAY_BUTTON:
                        return flappyDotGame.action_button_press()
                    else:
                        flappyDotGame.stop_game()
                        self.display_info.show()
                elif not flappyDotGame.is_game_enabled and key_name == SHOW_GAME_BUTTON:
                    flappyDotGame.start_game()

        if key_value and key_name not in self.__pressed_keys:
            if len(self.__pressed_keys) > 5:
                #TODO: map all keys there
                self.__send_key(self.__pressed_keys[0], False)
                self.__pressed_keys.remove(self.__pressed_keys[0])

            self.__pressed_keys.append(key_name)
            self.__send_key(key_name, key_value)
        elif not key_value and key_name in self.__pressed_keys:
            self.__pressed_keys.remove(key_name)
            self.__send_key(key_name, key_value)

    def __send_key (self, key_name, key_value):
        action = "press" if key_value else "release"
        key_code = getattr(Keycode, key_name, None)
        consumer_key_code = getattr(ConsumerControlCode, key_name, None)

        try:
            if key_code:
                getattr(keyboard_control, action)(key_code)
            elif consumer_key_code:
                if self.__media_key_pressed and key_value:
                    consumer_control.release(self.__media_key_pressed)
                self.__media_key_pressed = key_name
                getattr(consumer_control, action)(consumer_key_code)
            elif key_name in LAYOUT_CONFIG:
                next_layout = key_name if key_value else DEFAULT_LAYOUT_KEY
                curren_layout_config = LAYOUT_CONFIG[self.layout]
                next_layout_config = LAYOUT_CONFIG[next_layout]

                for row_index, row in enumerate(curren_layout_config):
                    for key_index, key in enumerate(row):
                        pressed_keys_copy = self.__pressed_keys.copy()
                        if key in pressed_keys_copy:
                            try:
                                new_key = next_layout_config[row_index][key_index]
                                if new_key != key:
                                    pressed_key_code = getattr(Keycode, key, None)
                                    new_key_key_code = getattr(Keycode, new_key, None)
                                    if pressed_key_code:
                                        keyboard_control.release(pressed_key_code)
                                        self.__pressed_keys.remove(key)
                                    if new_key_key_code:
                                        keyboard_control.press(new_key_key_code)
                                        self.__pressed_keys.append(new_key)
                            except IndexError:
                                pass
                self.layout = next_layout
        except OSError:
            self.__pressed_keys.remove(key_name)
