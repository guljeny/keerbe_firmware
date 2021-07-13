import busio
import displayio
import adafruit_displayio_ssd1306
from modules.i2c_bus import I2CBus
# from adafruit_bus_device import i2c_device
from constants import EXTERNAL_SCL, EXTERNAL_SDA, DISPLAY_ADDRESS, MEMORY_ADDRESS, DISPLAY_WIDTH, DISPLAY_HEIGHT

displayio.release_displays()

i2c = busio.I2C(scl=EXTERNAL_SCL, sda=EXTERNAL_SDA)

# while not i2c.try_lock():
#     print('try lock in displayController')
#     pass

# devices = i2c.scan()
# print('devices: ', devices)

# i2c.unlock()

display_bus = displayio.I2CDisplay(i2c, device_address=DISPLAY_ADDRESS)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

memory = I2CBus(i2c, MEMORY_ADDRESS)
