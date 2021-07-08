# import time

from modules.key_listener import KeyListener
from modules.keyboard import keyboard
from controllers.keyboardController import keyboard_controller
from constants import CONFIG_FILE, ROW_PINS, COLUMN_PINS
from modules.event_loop import event_loop

KeyListener(ROW_PINS, COLUMN_PINS, keyboard_controller.handle_key)

event_loop.start_ifinity_loop()

# def test():
#     i = 100000
#     startTime = time.monotonic()
#     while i > 0:
#         i -= 1
#     endTime = time.monotonic()
#     return endTime - startTime

# print(test())

# while True:
#     print("check", time.monotonic())
