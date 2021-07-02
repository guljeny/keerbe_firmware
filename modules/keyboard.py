import digitalio
import board
import usb_hid
import json
from functools import reduce
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl

DEFAULT_LAYOUT_KEY = "default"
ROW_PINS    = [board.GP0, board.GP1]
COLUMN_PINS = [board.GP2, board.GP3]

config_file = open('../layout.json')
config_data = config_file.read()
config = json.loads(config_data)
print(config)
layout_config = config.get('layout', {})
key_map = config.get('key_map', [])
print(layout_config)

layout_key = DEFAULT_LAYOUT_KEY
pressed_keys = []
released_keys = {}
media_key_pressed = None


kbd = Keyboard(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

row_pins    = []
column_pin = []

def show_game ():
    print("It's show game function")

SYS_ACTIONS = {
    "SHOW_GAME": show_game
}

for pin in ROW_PINS:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row_pins.append(row)

for pin in COLUMN_PINS:
    column = digitalio.DigitalInOut(pin)
    column.direction = digitalio.Direction.INPUT
    column.pull = digitalio.Pull.DOWN
    column_pin.append(column)

def key_press (key_name):
    global media_key_pressed
    global layout_key
    global SYS_ACTIONS

    key_code = getattr(Keycode, key_name, None)
    consumer_key_code = getattr(ConsumerControlCode, key_name, None)
    print("press key", key_name)

    if key_code:
        kbd.press(key_code)
    elif consumer_key_code:
        if media_key_pressed:
            key_release(media_key_pressed)
        media_key_pressed = key_name
        consumer_control.press(consumer_key_code)
    elif key_name in SYS_ACTIONS:
        SYS_ACTIONS[key_name]()
    elif key_name in layout_config:
        layout_key = key_name

def key_release (key_name):
    global media_key_pressed
    if not key_name: return
    key_code = getattr(Keycode, key_name, None)
    consumer_key_code = getattr(ConsumerControlCode, key_name, None)
    print("release key: ", key_name)

    if key_code:
        kbd.release(key_code)
    elif consumer_key_code:
        media_key_pressed = None
        consumer_control.release()
    elif key_name in layout_config:
        layout_key = DEFAULT_LAYOUT_KEY

def compare_arrays (a1, a2):
    a1.sort()
    a2.sort()
    return a1 == a2

def get_combination (key_name, pressed_keys):
    for key_group in key_map:
        if compare_arrays(key_group.get('combination', None), pressed_keys):
            return key_group.get('command', None)
    return None

def loop():
    global pressed_keys
    global released_keys
    global layout_key

    layout = layout_config[layout_key]

    if layout:
        for row_index in range(len(row_pins)):
            row = row_pins[row_index]
            row.value = True
            for column_index in range(len(column_pin)):
                column = column_pin[column_index]
                key_name = layout[row_index][column_index]
                if column.value:
                    if key_name not in pressed_keys:
                        pressed_keys.append(key_name)
                        key_name = get_combination(key_name, pressed_keys) or key_name
                        key_press(key_name)
                else:
                    released_keys[key_name] = released_keys[key_name] + 1 if released_keys.get(key_name, None) else 1
            row.value = False

    for key_name, released_count in released_keys.items():
        total_keys = reduce(lambda acc, row: acc + row.count(key_name), layout, 0)
        if released_keys[key_name] == total_keys and key_name in pressed_keys:
            pressed_keys.remove(key_name)
            key_release(key_name)
            key_release(get_combination(key_name, pressed_keys + [key_name]))
    released_keys = {}
