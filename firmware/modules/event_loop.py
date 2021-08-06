class EventLoop ():
    def __init__(self):
        self.events = []

    def append(self, event):
        self.events.append(event)

    def remove(self, event):
        if event in self.events:
            self.events.remove(event)

    def start_ifinity_loop(self):
        while True:
            for event in self.events:
                event()

event_loop = EventLoop()
