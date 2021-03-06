import busio
import displayio
import adafruit_displayio_ssd1306
from modules.i2c_bus import I2CBus
from controllers.uartController import UartController
from constants import EXTERNAL_SCL, EXTERNAL_SDA, DISPLAY_ADDRESS, MEMORY_ADDRESS, DISPLAY_WIDTH, DISPLAY_HEIGHT, SECOND_PART_RX

displayio.release_displays()

second_part_uart = busio.UART(rx=SECOND_PART_RX)
second_part = UartController(second_part_uart)

i2c = busio.I2C(scl=EXTERNAL_SCL, sda=EXTERNAL_SDA, frequency=200_000)

display_bus = displayio.I2CDisplay(i2c, device_address=DISPLAY_ADDRESS)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

memory = I2CBus(i2c, MEMORY_ADDRESS)
