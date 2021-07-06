# import digitalio
# import random
import board
# import usb_hid
# import time
# import adafruit_ssd1306
# import busio
# import digitalio
# import displayio
# import adafruit_displayio_ssd1306
# import terminalio
# from adafruit_display_text import label
# from adafruit_display_shapes import rect
from modules import kbd

ROW_PINS    = [board.GP0]
COLUMN_PINS = [board.GP1]

keyboard = kbd.Kbd(ROW_PINS, COLUMN_PINS)

while True:
    keyboard.check()
