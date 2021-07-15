from serial import Serial
import serial.tools.list_ports
import os

board_name = "Pico - CircuitPython CDC data"
board_name_two = "Pico - CircuitPython CDC2 data"

ports = serial.tools.list_ports.comports()
ports = serial.tools.list_ports.comports()

device_port = '/dev/cu.usbmodem14303'
# for device, name, description in serial.tools.list_ports.comports():
#     # print(device, ':', name, ':', description)
#     if name == board_name or name == board_name_two:
#         device_port = device
#         break

print(device_port)

serial = Serial(device_port)

files_to_send = [
    "./code.py",
    "./boot.py",
    "./utils.py",
    "./constants.py",
    "./modules",
    "./controllers",
    # "./lib",
]

excluded_files = [
    "__pycache__",
    ".DS_Store",
]


serial.close()
serial.open()

serial.reset_input_buffer()
serial.reset_output_buffer()


def await_answer ():
    while not serial.in_waiting:
        pass
    return serial.read(serial.in_waiting)

# serial.write(b'CLEAN')
# await_answer()

def send_file (file_path):
    print(file_path)
    serial.write(b'FLASH')
    await_answer()
    file = open(file_path, "rb")
    file_content = file.read()
    serial.write(file_path.encode('utf-8'))
    await_answer()
    serial.write(file_content)
    await_answer()

def map_files_list(files_list = files_to_send, prev_path = ""):
    for path_dir in files_list:
        current_path = os.path.join(prev_path, path_dir)
        if path_dir not in excluded_files and current_path not in excluded_files:
            if os.path.isdir(current_path):
                map_files_list(os.listdir(current_path), current_path)
            else:
                send_file(current_path)

map_files_list()

serial.write(b'REEBOT')
print('finish write')
serial.close()
