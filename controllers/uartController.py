from modules.event_loop import event_loop

class UartController():
    def __init__(self, uart, length = 3):
        self.uart = uart
        self.length = length
        self.on_read = None
        self.queue = []
        event_loop.append(self.__loop)

    def __loop(self):
        if self.uart.in_waiting:
            for val in self.uart.read(self.uart.in_waiting):
                self.queue.append(val)

        if len(self.queue) >= self.length and self.on_read:
            args = []
            for i in range(self.length):
                args.append(self.queue.pop(0))
            self.on_read(*args)
                    
                    
