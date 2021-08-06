import sys, time, os
import serial.tools.list_ports
from serial import Serial

board_name_selector_v1 = "Pico - CircuitPython CDC data"
board_name_selector_v2 = "Pico - CircuitPython CDC2 data"

dir = os.path.dirname(os.path.abspath(__file__))

def prepare_path (path):
    return os.path.normpath(os.path.join(dir, '../firmware/', path))

def check_ok_answer (answer):
    return answer == b'OK'

def await_answer(serial_port, timeout = 3.0):
    start_time = time.monotonic()
    while not serial_port.in_waiting and start_time + timeout > time.monotonic():
        pass
    return serial_port.read(serial_port.in_waiting) or None

def continue_read (serial_port, timeout = 0.3):
    start_time = time.monotonic()
    while not serial_port.in_waiting and start_time + timeout > time.monotonic():
        pass
    return serial_port.read(serial_port.in_waiting) or None

def scan():
    serial_port = None
    device_type = None
    try:
        for device, name, description in serial.tools.list_ports.comports():
            if name == board_name_selector_v1 or name == board_name_selector_v2:
                serial_port = Serial(device)
                serial_port.close()
                serial_port.open()
                serial_port.reset_input_buffer()
                serial_port.reset_output_buffer()
                serial_port.write(b'TYPE')
                device_type = await_answer(serial_port, 1.0)
                if device_type:
                    device_type = device_type.decode('utf-8')
                    print('{"serial": "' + device + '", "type":"' + device_type + '"}')
                    sys.stdout.flush()
                    break
    except:
        pass
    if not device_type:
        print('{}')
        sys.stdout.flush()

class FlashTool ():
    def __init__(self, port):
        self.serial_port = Serial(port)

    def clean(self):
        self.serial_port.write(b'CLEAN')
        answer = await_answer(self.serial_port, 600.0)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot clean memory')

    def reset_memory(self):
        self.serial_port.write(b'RESET_MEMORY')

    def reboot(self):
        self.serial_port.write(b'REBOOT')

    def get_layout(self):
        self.serial_port.write(b'LAYOUT')
        file_content = ""
        next_content = await_answer(self.serial_port)
        while next_content:
            file_content += next_content.decode('utf-8')
            next_content = continue_read(self.serial_port)
        print(file_content)

    def send_file (self, file_path, file_content = None):
        print(file_path)
        sys.stdout.flush()
        self.serial_port.write(b'FLASH')
        answer = await_answer(self.serial_port)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot start flashing')
        if not file_content:
            file = open(prepare_path(file_path), "rb")
            file_content = file.read()
        else:
            file_content = file_content.encode()
        self.serial_port.write(file_path.encode('utf-8'))
        answer = await_answer(self.serial_port)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot send path')
        self.serial_port.write(file_content)
        answer = await_answer(self.serial_port, 30.0)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot send file')
