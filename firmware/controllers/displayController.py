import busio
import displayio
# import adafruit_displayio_ssd1306
# from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, EXTERNAL_SCL, EXTERNAL_SDA
from utils import clear_display_group
from modules.i2c_device import display

# displayio.release_displays()
# i2c = busio.I2C(scl=EXTERNAL_SCL, sda=EXTERNAL_SDA) # This RPi Pico way to call I2C
# i2c.try_lock()
# devices = i2c.scan()
# i2c.unlock()
# display_bus = displayio.I2CDisplay(i2c, device_address=devices[0])
# display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)
# print(display.time_to_refresh)

class DisplayController():
    def __init__(self):
        self.main_screen = displayio.Group()
        display.show(self.main_screen)

    def show(self, group):
        if group not in self.main_screen:
            clear_display_group(self.main_screen)
            self.main_screen.append(group)

    def sleep(self):
        if display.is_awake:
            display.sleep()

    def wake(self):
        if not display.is_awake:
            display.wake()

displayController = DisplayController()
