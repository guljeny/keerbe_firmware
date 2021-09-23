class I2CBus():
    def __init__(self, i2c, adress):
        self.i2c = i2c
        self.adress = adress

    def write_then_read(self, bytearray, result):
        self.i2c.writeto_then_readfrom(self.adress, bytearray, result)

    def write(self, bytearray):
        try:
            self.i2c.writeto(self.adress, bytearray)
        except OSError:
            return

    def try_lock(self):
        return self.i2c.try_lock()

    def unlock(self):
        self.i2c.unlock()
