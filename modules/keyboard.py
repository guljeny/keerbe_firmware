import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard as KeyboardControl
from adafruit_hid.consumer_control import ConsumerControl
from constants import DEFAULT_LAYOUT_KEY, GAME_PLAY_BUTTON, SHOW_GAME_BUTTON, LAYOUT_CONFIG
from controllers.keyboardController import keyboard_controller
from modules.flappyDotGame import FlappyDotGame
from modules.display_info import display_info

keyboard_control = KeyboardControl(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)


flappyDotGame = FlappyDotGame()

class Keyboard ():
    def __init__(self):
        self.is_game_mode = False
        self.__media_key_pressed = None
        keyboard_controller.subscribe(self.__handle_key_press)
        display_info.show()

    def __handle_key_press (self, key_name, key_value):
        action = "press" if key_value else "release"
        key_code = getattr(Keycode, key_name, None)
        consumer_key_code = getattr(ConsumerControlCode, key_name, None)

        if key_value:
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

keyboard = Keyboard()
