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

# print(usb_hid.Device.KEYBOARD)
# usb_hid.enable((usb_hid.Device.CONSUMER_CONTROL), boot_device = 0)

storage.remount("/", readonly = False, disable_concurrent_write_protection = True)
supervisor.disable_autoreload()


if not button.value:
    print('boot as keyboard')
    usb_cdc.enable(console=False, data=False)
    usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.CONSUMER_CONTROL), boot_device = 1)
    # usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device = 1)
    # usb_cdc.enable(console=False, data=True)
    storage.disable_usb_drive()
    supervisor.set_next_code_file('./main.py')
else:
    print('boot in dev')
    usb_cdc.enable(console=True, data=True)
    # usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.CONSUMER_CONTROL))
    supervisor.set_next_code_file('./flash.py')

output.deinit()
button.deinit()
