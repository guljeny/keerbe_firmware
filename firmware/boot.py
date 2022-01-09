import usb_hid
import usb_cdc
import storage
import supervisor
from constants import ROW_PINS, COLUMN_PINS
import digitalio
import supervisor

output = digitalio.DigitalInOut(ROW_PINS[0])
output.direction = digitalio.Direction.OUTPUT
output.value = 1

button = digitalio.DigitalInOut(COLUMN_PINS[0])
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

storage.remount("/", readonly = False, disable_concurrent_write_protection = True)
supervisor.disable_autoreload()


if not button.value:
    usb_cdc.enable(console=True, data=True)
    supervisor.set_next_code_file('./flash.py')
else:
    usb_cdc.enable(console=False, data=False)
    usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.CONSUMER_CONTROL), boot_device = 1)
    storage.disable_usb_drive()
    supervisor.set_next_code_file('./main.py')

output.deinit()
button.deinit()
