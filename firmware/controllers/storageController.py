import time
from modules.external_device import memory
from constants import MEMORY_ADDRESS
from modules.event_loop import event_loop

delay = 1.0

class StorageController():
    def __init__ (self):
        self.read_tasks = []
        self.write_tasks = []
        event_loop.append(self.__loop)

    def write (self, data, start_bit = 0):
        self.write_tasks.append((data, start_bit))

    def sync_write(self, data, start_bit = 0):
        while not memory.try_lock():
            pass
        memory.write(bytes([start_bit] + data))
        memory.unlock()

    def read (self, callback, length = 1, start_bit = 0):
        self.read_tasks.append((callback, length, start_bit))

    def __loop(self):
        if not len(self.write_tasks) and not len(self.read_tasks):
            return False

        if not memory.try_lock():
            return False

        if len(self.write_tasks):
            data, start_bit = self.write_tasks[0]
            memory.write(bytes([start_bit] + data))
            self.write_tasks.remove((data, start_bit))

        if len(self.read_tasks):
            for callback, length, start_bit in self.read_tasks:
                try:
                    result = bytearray(length)
                    memory.write_then_read(bytes([start_bit]), result)
                    callback(result)
                    self.read_tasks.remove((callback, length, start_bit))
                    break
                except OSError:
                    pass

        memory.unlock()

storage_controller = StorageController()
