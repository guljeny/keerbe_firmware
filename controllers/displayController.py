import busio
import displayio
import adafruit_displayio_ssd1306
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_SCL, DISPLAY_SDA
from utils import clear_display_group

displayio.release_displays()
i2c = busio.I2C(scl=DISPLAY_SCL, sda=DISPLAY_SDA) # This RPi Pico way to call I2C
i2c.try_lock()
devices = i2c.scan()
i2c.unlock()
display_bus = displayio.I2CDisplay(i2c, device_address=devices[0])
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

class DisplayController():
    def __init__(self):
        self.main_screen = displayio.Group()
        display.show(self.main_screen)

    def show(self, group):
        clear_display_group(self.main_screen)
        self.main_screen.append(group)

displayController = DisplayController()
