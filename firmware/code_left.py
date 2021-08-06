import board
import busio
from modules.key_listener import KeyListener
from modules.event_loop import event_loop
from constants import ROW_PINS, COLUMN_PINS, SECOND_PART_TX



second_part = busio.UART(tx = SECOND_PART_TX)

def handle_key(key_value, row, column):
    print(key_value, row, column)
    second_part.write(bytearray([1 if key_value else 0, row, column]))


KeyListener(ROW_PINS, COLUMN_PINS, handle_key)

event_loop.start_ifinity_loop()
