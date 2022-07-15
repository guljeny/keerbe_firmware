from modules.key_listener import KeyListener
from modules.keyboard import Keyboard
from constants import ROW_PINS, COLUMN_PINS
from modules.external_device import second_part

keyboard = Keyboard()

def listen_key_from_main_part (value, row, column):
    keyboard.handle_key(value, row, column + len(COLUMN_PINS))

KeyListener(ROW_PINS, COLUMN_PINS, listen_key_from_main_part)

second_part.on_read = keyboard.handle_key
