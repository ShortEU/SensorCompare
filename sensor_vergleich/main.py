from machine import Pin, I2C
from ina219 import INA219
from aht10 import AHT10
import time

# I2C initialisieren
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
ina = INA219(i2c, addr=0x40)
aht = AHT10(i2c)

while True:
    voltage = ina.getBusVoltage_V()
    current = ina.getCurrent_mA()
    temperature, humidity = aht.read()

    # Seriell im CSV-Format ausgeben (für den PC!)
    print(f"{voltage:.2f},{current:.2f},{temperature:.2f},{humidity:.2f}")

    time.sleep(5)