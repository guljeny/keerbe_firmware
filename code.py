import digitalio
import board
import usb_hid
import time
import rotaryio
from modules import keyboard

# encoder = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
# last_position = 0

# left = digitalio.DigitalInOut(board.GP0)
# left.direction = digitalio.Direction.INPUT
# left.pull = digitalio.Pull.UP

# right = digitalio.DigitalInOut(board.GP1)
# right.direction = digitalio.Direction.INPUT
# right.pull = digitalio.Pull.UP

# encoder_state = []

# base = digitalio.DigitalInOut(board.GP2)
# base.direction = digitalio.Direction.OUTPUT

# base.value = True

while True:
    # if len(encoder_state):
    #     if encoder_state[0] == False and encoder_state[1] == False and left.value == True and right.value == False:
    #         print("right")
    #     if encoder_state[0] == True and encoder_state[1] == False and left.value == False and right.value == False:
    #         print("left")
    # if encoder.position > last_position:
    # if encoder.position < last_position:
    # last_position = encoder.position
    # encoder_state = [left.value, right.value]

    keyboard.loop()
    # time.sleep(0.01)

# **
# *
# * OLED control
# *

# import adafruit_ssd1306
# import busio
# import displayio

# i2c = busio.I2C(scl=board.GP5, sda=board.GP4) # This RPi Pico way to call I2C
# oled = adafruit_ssd1306.SSD1306_I2C(width=128, height=32, i2c=i2c)

# oled.fill(1)
# oled.pixel(0, 0, 1)
# oled.pixel(4, 0, 1)
# oled.pixel(7, 3, 1)
# oled.text("nastya", 0, 0)
# oled.show()
