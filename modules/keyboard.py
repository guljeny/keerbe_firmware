import digitalio
import board
import usb_hid
import json
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

layoutFile = open('../layout.json')
parsedLayout = layoutFile.read()
print(parsedLayout)
layout_object = json.loads(parsedLayout)

layout = []
for row in layout_object:
    builtin_row = []
    for key in row:
        builtin_row.append(getattr(Keycode, key))
    layout.append(builtin_row)


layout = [
    [Keycode.SHIFT, Keycode.W],
    [Keycode.A, Keycode.S],
]

row_pins    = [board.GP0, board.GP1]
column_pins = [board.GP2, board.GP3]

kbd = Keyboard(usb_hid.devices)

rows    = []
columns = []

for row_pin in row_pins:
    row = digitalio.DigitalInOut(row_pin)
    row.direction = digitalio.Direction.OUTPUT
    rows.append(row)

for column_pin in column_pins:
    column = digitalio.DigitalInOut(column_pin)
    column.direction = digitalio.Direction.INPUT
    column.pull = digitalio.Pull.DOWN
    columns.append(column)

def loop():
    for row_index in range(len(rows)):
        row = rows[row_index]
        row.value = True
        for column_index in range(len(columns)):
            column = columns[column_index]
            if column.value:
                kbd.press(layout[row_index][column_index])
            else:
                kbd.release(layout[row_index][column_index])
        row.value = False
