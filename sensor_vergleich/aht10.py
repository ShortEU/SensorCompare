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

        # Rohdaten für Temperatur zusammensetzen
        temp_high = data[3] & 0x0F     # untere 4 Bits von data[3]
        temp_mid  = data[4]            # ganzes Byte
        temp_low  = data[5]            # ganzes Byte
        raw_temp = (temp_high << 16) | (temp_mid << 8) | temp_low

        # Rohdaten für Feuchte zusammensetzen
        humi_high = data[1]            # ganzes Byte
        humi_mid  = data[2]            # ganzes Byte
        humi_low  = data[3] >> 4       # obere 4 Bits von data[3]
        raw_humi = (humi_high << 12) | (humi_mid << 4) | humi_low

        temperature = (raw_temp / 1048576.0) * 200.0 - 50.0
        humidity = (raw_humi / 1048576.0) * 100.0

        return temperature, humidity
