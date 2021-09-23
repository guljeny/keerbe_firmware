import busio
import displayio
from utils import clear_display_group
from modules.external_device import display

class DisplayController():
    def __init__ (self):
        self.main_screen = displayio.Group()
        display.show(self.main_screen)

    def show (self, group):
        if group not in self.main_screen:
            clear_display_group(self.main_screen)
            self.main_screen.append(group)

    def sleep (self):
        if display.is_awake:
            display.sleep()

    def wake (self):
        if not display.is_awake:
            display.wake()

    @property
    def is_awake (self):
        return display.is_awake

displayController = DisplayController()
