import time
import serial.tools.list_ports
from serial import Serial

board_name_selector_v1 = "Pico - CircuitPython CDC data"
board_name_selector_v2 = "Pico - CircuitPython CDC2 data"

def check_ok_answer (answer):
    return answer == b'OK'

class FlashTool ():
    def __init__(self):
        self.device_type = None
        self.serial = None
        for device, name, description in serial.tools.list_ports.comports():
            if name == board_name_selector_v1 or name == board_name_selector_v2:
                self.serial = Serial(device)
                self.serial.close()
                self.serial.open()
                self.serial.reset_input_buffer()
                self.serial.reset_output_buffer()
                self.serial.write(b'TYPE')
                self.device_type = self.__await_answer__()
                if self.device_type:
                    print('device serial: ', device)
                    self.device_type = self.device_type.decode('utf-8')
                    break

    def __await_answer__(self, timeout = 3.0):
        start_time = time.monotonic()
        while not self.serial.in_waiting and start_time + timeout > time.monotonic():
            pass
        return self.serial.read(self.serial.in_waiting) or None
    
    def clean(self):
        self.serial.write(b'CLEAN')
        answer = self.__await_answer__(600.0)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot clean memory')

    def reset_memory(self):
        self.serial.write(b'RESET_MEMORY')

    def reboot(self):
        self.serial.write(b'REBOOT')

    def send_file (self, file_path):
        print(file_path)
        self.serial.write(b'FLASH')
        answer = self.__await_answer__()
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot start flashing')
        file = open(file_path, "rb")
        file_content = file.read()
        self.serial.write(file_path.encode('utf-8'))
        answer = self.__await_answer__()
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot send path')
        self.serial.write(file_content)
        answer = self.__await_answer__(30.0)
        if not check_ok_answer(answer):
            raise Exception('FlashError', 'cannot send file')
