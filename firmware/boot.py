import usb_hid
import usb_cdc
import storage
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

print(button.value);

if button.value:
    usb_cdc.enable(console=True, data=True)
    supervisor.set_next_code_file('empty_run.py')
else:
    print('w/o button')
    storage.disable_usb_drive()
    usb_cdc.enable(console=True, data=True)
    usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.CONSUMER_CONTROL), boot_device = 1)
    supervisor.set_next_code_file('code.py')

output.deinit()
button.deinit()
