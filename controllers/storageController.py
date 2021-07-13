import time
from modules.i2c_device import memory
from constants import MEMORY_ADDRESS
from modules.event_loop import event_loop

delay = 1.0

class StorageController():
    def __init__ (self):
        # self.last_call = 0
        self.read_tasks = []
        self.write_tasks = []
        event_loop.append(self.__loop)

    def write (self, data, start_bit = 0):
        self.write_tasks.append((data, start_bit))
        # memory.write(bytes([start_bit] + data))

    def read (self, callback, length = 1, start_bit = 0):
        self.read_tasks.append((callback, length, start_bit))
        result = bytearray(length)
        # timestamp = time.monotonic()
        # while time.monotonic() < timestamp + delay:
        #     try:
        #         memory.write_then_readinto(bytes([start_bit]), result)
        #         break
        #     except OSError:
        #         pass

        # print('read_from', result)
        # return result

    def __loop(self):
        # now = time.monotonic()
        # print(self.last_call + delay, 'started at: ', now)
        if not len(self.write_tasks) and not len(self.read_tasks):
            return False

        if not memory.try_lock():
            return False
            # print('not memory lock')

        # if self.last_call + delay > now:
        #     print('fuck if')
        #     return False

        # print('ok')
        # self.last_call = now
        # print('locked')

        if len(self.write_tasks):
            data, start_bit = self.write_tasks[0]
            memory.write(bytes([start_bit] + data))
            self.write_tasks.remove((data, start_bit))

        if len(self.read_tasks):
            for callback, length, start_bit in self.read_tasks:
                try:
                    result = bytearray(length)
                    # memory.write_then_readinto(bytes([start_bit]), result)
                    memory.write_then_read(bytes([start_bit]), result)
                    callback(result)
                    self.read_tasks.remove((callback, length, start_bit))
                    break
                except OSError:
                    pass

        memory.unlock()

storage_controller = StorageController()
