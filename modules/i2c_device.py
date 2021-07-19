import busio
import displayio
import adafruit_displayio_ssd1306
from modules.i2c_bus import I2CBus
from controllers.uartController import UartController
from constants import EXTERNAL_SCL, EXTERNAL_SDA, DISPLAY_ADDRESS, MEMORY_ADDRESS, DISPLAY_WIDTH, DISPLAY_HEIGHT, SECOND_PART_RX, SECOND_PART_TX

displayio.release_displays()

i2c = busio.I2C(scl=EXTERNAL_SCL, sda=EXTERNAL_SDA)
second_part_uart = busio.UART(rx=SECOND_PART_RX)
second_part = UartController(second_part_uart)

display_bus = displayio.I2CDisplay(i2c, device_address=DISPLAY_ADDRESS)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

memory = I2CBus(i2c, MEMORY_ADDRESS)
