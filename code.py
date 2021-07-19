from modules.key_listener import KeyListener
from modules.keyboard import keyboard
from controllers.serialController import serial_loop
from controllers.keyboardController import keyboard_controller
from constants import ROW_PINS, COLUMN_PINS
from modules.event_loop import event_loop
from modules.i2c_device import second_part


def listen_key_from_main_part (value, row, column):
    keyboard_controller.handle_key(value, row, column + len(COLUMN_PINS))

KeyListener(ROW_PINS, COLUMN_PINS, listen_key_from_main_part)

second_part.on_read = keyboard_controller.handle_key

event_loop.append(serial_loop)
event_loop.start_ifinity_loop()
