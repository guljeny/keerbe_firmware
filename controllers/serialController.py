import os
import re
import supervisor
from usb_cdc import data as serial

class PathInfo ():
    def __init__(self, path):
        self.path = path.replace('./', '')
        parts = self.path.split('/')
        dir_parts = parts[:-1] if len(parts) else []
        self.is_dir = False
        try:
            os.listdir(path)
            self.is_dir = True
        except OSError:
            pass

        self.prev_dirs = []
        for dir in dir_parts:
            self.prev_dirs.append((self.prev_dirs[-1] if len(self.prev_dirs) else ".") + os.sep + dir)

        self.dir = (os.sep).join(dir_parts) if len(dir_parts) else ""
        self.parent_dir_exists = False
        try:
            len(os.listdir(self.dir))
            self.parent_dir_exists = True
        except OSError:
            pass

def send_ok():
    serial.write(b'OK')

def await_answer ():
    while not serial.in_waiting:
        pass
    return serial.read(serial.in_waiting)

def continue_read ():
    if not serial.in_waiting:
        return False
    return serial.read(serial.in_waiting)

def cleanup (path_list = os.listdir('./'), prev_path=""):
    for path in path_list:
        current_path = prev_path + (os.sep if prev_path else "") + path
        path_info = PathInfo(current_path)
        if path_info.is_dir:
            cleanup(os.listdir(current_path), current_path)
            try:
                os.rmdir(current_path)
            except OSError:
                pass
        else:
            try:
                os.remove(current_path)
            except OSError:
                pass

def serial_loop():
    if not serial.in_waiting:
        return
    command = serial.read(serial.in_waiting)
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
            print('create_dir', path_info.prev_dirs)
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
        cleanup()
        send_ok()
    elif command == b'REEBOT':
        supervisor.reload()
