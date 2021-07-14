from modules.key_listener import KeyListener
from modules.keyboard import keyboard
from controllers.serialController import serial_loop
from controllers.keyboardController import keyboard_controller
from constants import CONFIG_FILE, ROW_PINS, COLUMN_PINS
from modules.event_loop import event_loop


KeyListener(ROW_PINS, COLUMN_PINS, keyboard_controller.handle_key)

event_loop.append(serial_loop)
event_loop.start_ifinity_loop()
