import digitalio
from modules.event_loop import event_loop

class KeyListener():
    def __init__(self, rows, columns, handle_key):
        self.handle_key = handle_key
        self.rows = []
        self.columns = []
        self.pressed_keys = []

        for pin in rows:
            row = digitalio.DigitalInOut(pin)
            row.direction = digitalio.Direction.OUTPUT
            self.rows.append(row)

        for pin in columns:
            column = digitalio.DigitalInOut(pin)
            column.direction = digitalio.Direction.INPUT
            column.pull = digitalio.Pull.DOWN
            self.columns.append(column)

        event_loop.append(self.check)

    def check(self):
        for row_index in range(len(self.rows)):
            row = self.rows[row_index]
            row.value = True
            for column_index in range(len(self.columns)):
                column = self.columns[column_index]
                value = column.value
                key_position = [row_index, column_index]
                if value:
                    if key_position not in self.pressed_keys:
                        self.pressed_keys.append(key_position)
                        self.handle_key(value, row_index, column_index)
                elif key_position in self.pressed_keys:
                    self.pressed_keys.remove(key_position)
                    self.handle_key(value, row_index, column_index)
            row.value = False
