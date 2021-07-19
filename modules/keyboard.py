import usb_hid
import time
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard as KeyboardControl
from adafruit_hid.consumer_control import ConsumerControl
from constants import DEFAULT_LAYOUT_KEY, SHOW_GAME_BUTTON, DISABLE_DISPLAY_BUTTON
from config import GAME_PLAY_BUTTON, LAYOUT_CONFIG, TIME_TO_DISPLAY_SLEEP
from controllers.keyboardController import keyboard_controller
from controllers.displayController import displayController
from modules.flappyDotGame import FlappyDotGame
from modules.display_info import display_info
from modules.event_loop import event_loop

keyboard_control = KeyboardControl(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

flappyDotGame = FlappyDotGame()

class Keyboard ():
    def __init__(self):
        self.display_is_enabled = True
        self.last_awake_time = time.monotonic()
        self.is_game_mode = False
        self.__media_key_pressed = None
        keyboard_controller.subscribe(self.__handle_key_press)
        display_info.show()
        event_loop.append(self.__keyboard_loop)

    def __handle_key_press (self, key_name, key_value):
        action = "press" if key_value else "release"
        key_code = getattr(Keycode, key_name, None)
        consumer_key_code = getattr(ConsumerControlCode, key_name, None)

        if key_value:
            if self.display_is_enabled:
                displayController.wake()
            self.last_awake_time = time.monotonic()
            if key_name == DISABLE_DISPLAY_BUTTON:
                if self.display_is_enabled:
                    self.display_is_enabled = False
                    displayController.sleep()
                else:
                    self.display_is_enabled = True
                    displayController.wake()
            if self.is_game_mode:
                if key_name == GAME_PLAY_BUTTON:
                    return flappyDotGame.action_button_press()
                else:
                    self.is_game_mode = False
                    flappyDotGame.stop_game()
                    display_info.show()
            elif not self.is_game_mode and key_name == SHOW_GAME_BUTTON:
                self.is_game_mode = True
                flappyDotGame.start_game()

        if key_code:
            getattr(keyboard_control, action)(key_code)
        elif consumer_key_code:
            if self.__media_key_pressed and key_value:
                self.__send_key(self.__media_key_pressed, False)
            self.__media_key_pressed = key_name
            getattr(consumer_control, "action")(consumer_key_code)
        elif key_name in LAYOUT_CONFIG:
            layout = LAYOUT_CONFIG[key_name] if key_value else LAYOUT_CONFIG[DEFAULT_LAYOUT_KEY]
            keyboard_controller.set_layout(layout)

    def __keyboard_loop(self):
        if self.last_awake_time + TIME_TO_DISPLAY_SLEEP < time.monotonic():
            displayController.sleep()

keyboard = Keyboard()
