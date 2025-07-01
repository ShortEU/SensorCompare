import time

class INA219:
    REG_CONFIG = 0x00
    REG_SHUNTVOLTAGE = 0x01
    REG_BUSVOLTAGE = 0x02
    REG_POWER = 0x03
    REG_CURRENT = 0x04
    REG_CALIBRATION = 0x05

    def __init__(self, i2c, addr=0x40):
        self.i2c = i2c
        self.addr = addr

        self._cal_value = 410  # Kalibrierwert (für 0.1 Ohm Shunt, 3.2A max)
        self._current_lsb = 0.001  # mA/bit
        self._power_lsb = 2.0  # mW/bit

        # Konfiguriere den Sensor
        config = (0b001 << 13) | (0b011 << 11) | (0b111 << 8) | (0b111 << 5) | 0b111
        self._write_register(self.REG_CONFIG, config)
        self._write_register(self.REG_CALIBRATION, self._cal_value)

    def _write_register(self, reg, value):
        buf = bytearray(2)
        buf[0] = (value >> 8) & 0xFF
        buf[1] = value & 0xFF
        self.i2c.writeto_mem(self.addr, reg, buf)

    def _read_register(self, reg):
        buf = self.i2c.readfrom_mem(self.addr, reg, 2)
        return (buf[0] << 8) | buf[1]

    def getBusVoltage_V(self):
        raw = self._read_register(self.REG_BUSVOLTAGE)
        return ((raw >> 3) * 4) / 1000  # Umrechnung auf Volt

    def getShuntVoltage_mV(self):
        raw = self._read_register(self.REG_SHUNTVOLTAGE)
        if raw > 32767:
            raw -= 65536
        return raw * 0.01  # Umrechnung auf mV

    def getCurrent_mA(self):
        self._write_register(self.REG_CALIBRATION, self._cal_value)
        raw = self._read_register(self.REG_CURRENT)
        if raw > 32767:
            raw -= 65536
        return raw * self._current_lsb

    def getPower_mW(self):
        self._write_register(self.REG_CALIBRATION, self._cal_value)
        raw = self._read_register(self.REG_POWER)
        return raw * self._power_lsb
