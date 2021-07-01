import usb_hid
import usb_cdc
import storage

usb_hid.enable((usb_hid.Device.KEYBOARD,))
usb_cdc.enable(console=True, data=True)

# storage.remount("/", readonly=False, True)

# m = storage.getmount("/")
# m.label = "MY_KBD"

# storage.remount("/", readonly=False)

