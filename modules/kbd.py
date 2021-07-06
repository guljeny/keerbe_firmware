import digitalio

class Kbd():
    def __init__(self, rows, columns):
        # self.on_press = on_press
        self.rows = []
        self.columns = []
        self.pressed_keys = []
        self.released_keys = []

        for pin in rows:
            row = digitalio.DigitalInOut(pin)
            row.direction = digitalio.Direction.OUTPUT
            self.rows.append(row)

        for pin in columns:
            column = digitalio.DigitalInOut(pin)
            column.direction = digitalio.Direction.INPUT
            column.pull = digitalio.Pull.DOWN
            self.columns.append(column)

    def check(self):
        released_keys = []
        for row_index in range(len(self.rows)):
            row = self.rows[row_index]
            row.value = True
            for column_index in range(len(self.columns)):
                column = self.columns[column_index]
                key_position = [row_index, column_index]
                # key_name = layout[row_index][column_index]
                # key_name = str(row_index) + str(column_index)
                if column.value:
                    if key_position not in self.pressed_keys:
                        self.pressed_keys.append(key_name)
                        pirnt("key press: ", key_position)
                        # key_name = get_combination(key_name, pressed_keys) or key_name
                        # key_press(key_name)
                else:
                    print("key release: ", key_position)
                    # self.released_keys[key_name] = released_keys[key_name] + 1 if released_keys.get(key_name, None) else 1
            row.value = False

        # for key_name, released_count in released_keys.items():
        #     total_keys = reduce(lambda acc, row: acc + row.count(key_name), layout, 0)
        #     if released_keys[key_name] == total_keys and key_name in pressed_keys:
        #         pressed_keys.remove(key_name)
        #         key_release(key_name)
        #         key_release(get_combination(key_name, pressed_keys + [key_name]))
        # released_keys = {}
