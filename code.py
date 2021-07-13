# import displayio
from modules.key_listener import KeyListener
from modules.keyboard import keyboard
from controllers.keyboardController import keyboard_controller
from constants import CONFIG_FILE, ROW_PINS, COLUMN_PINS
from modules.event_loop import event_loop

# displayio.release_displays()

KeyListener(ROW_PINS, COLUMN_PINS, keyboard_controller.handle_key)

event_loop.start_ifinity_loop()

# import board
# import busio
# import digitalio
# import time


# i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
# devices = i2c.scan()
# print(devices)

# _value = 12312112
# print(_value)
# _v_b = []
# for el in list(str(_value)):
#     _v_b.append(int(el))
# _bytes = [1] + _v_b

# i2c.writeto(80, bytes(_bytes))
# timestamp = time.monotonic()
# result = bytearray(8)
# while time.monotonic() < timestamp + 1.0:
#     try:
#         # i2c.writeto(80, bytes([1]), end=1)
#         i2c.writeto_then_readfrom(0x50, bytes([1]), result)
#         break
#     except OSError:
#         pass
# print(result)

# _result = ''
# for _byte in result:
#     _result += str(_byte)

# print(int(_result))


# i2c.unlock()
