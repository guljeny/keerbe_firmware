from controllers.serialController import serial_loop
from modules.event_loop import event_loop

event_loop.append(serial_loop)
event_loop.start_ifinity_loop()
