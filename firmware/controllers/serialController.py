import os
import re
import microcontroller
import time
from constants import MEMORY_SIZE
from usb_cdc import data as serial
from controllers.storageController import storage_controller
from modules.file_system import PathInfo, cleanup_dir
from config import config_data

def reset_serial():
    try:
        serial.reset_input_buffer()
        serial.reset_output_buffer()
    except OSError:
        time.sleep(1)
        reset_serial()

reset_serial()

def send_ok():
    serial.write(b'OK')

def await_answer ():
    while not serial.in_waiting:
        pass
    return serial.read(serial.in_waiting)

def continue_read ():
    if not serial.in_waiting:
        return None
    return serial.read(serial.in_waiting)


def serial_loop():
    if not serial.in_waiting:
        return
    command = serial.read(serial.in_waiting)
    print(command)
    if command == b'FLASH':
        send_ok()
        file_path = await_answer()
        path = file_path.decode("utf-8")
        send_ok()
        file_content = ""
        next_content = await_answer()
        while next_content:
            file_content += next_content.decode('utf-8')
            next_content = continue_read()

        path_info = PathInfo(path)
        if not path_info.parent_dir_exists:
            for prev_dir in path_info.prev_dirs:
                try:
                    os.mkdir(prev_dir)
                except OSError:
                    pass
        f = open(path, 'w')
        f.write(file_content)
        f.close()
        send_ok()
    elif command == b'CLEAN':
        cleanup_dir()
        send_ok()
    elif command == b'RESET_MEMORY':
        storage_controller.sync_write([0] * MEMORY_SIZE)
        time.sleep(1)
        microcontroller.reset()
    elif command == b'TYPE':
        serial.write(b'KEEBEE_1')
    elif command == b'LAYOUT':
        for l in config_data:
            serial.write(l.encode())
    elif command == b'REBOOT':
        microcontroller.reset()
    elif command:
        print('delete', command)
        serial.reset_input_buffer()
        serial.reset_output_buffer()
