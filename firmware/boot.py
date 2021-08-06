import usb_hid
import usb_cdc
import storage
import supervisor
from constants import ROW_PINS, COLUMN_PINS
import digitalio

output = digitalio.DigitalInOut(ROW_PINS[0])
output.direction = digitalio.Direction.OUTPUT
output.value = 1

button = digitalio.DigitalInOut(COLUMN_PINS[0])
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL))
usb_cdc.enable(console=True, data=True)

storage.remount("/", readonly = False, disable_concurrent_write_protection = True)
supervisor.disable_autoreload()

if not button.value:
    storage.disable_usb_drive()

output.deinit()
button.deinit()
