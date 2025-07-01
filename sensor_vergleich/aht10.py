import time
import struct

class AHT10:
    def __init__(self, i2c, address=0x38):
        self.i2c = i2c
        self.address = address
        self._init_sensor()

    def _init_sensor(self):
        try:
            self.i2c.writeto(self.address, bytearray([0xE1, 0x08, 0x00]))
            time.sleep(0.01)
        except:
            pass

    def read(self):
        self.i2c.writeto(self.address, b'\xAC\x33\x00')
        time.sleep(0.08)
        data = self.i2c.readfrom(self.address, 6)

        status = data[0]
        if (status & 0x80) == 0x80:
            raise Exception("AHT10 is busy")

        raw_temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
        raw_humi = (data[1] << 12) | (data[2] << 4) | (data[3] >> 4)

        temperature = (raw_temp / 1048576.0) * 200.0 - 50.0
        humidity = (raw_humi / 1048576.0) * 100.0

        return temperature, humidity
