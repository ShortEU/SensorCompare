import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Serielle Verbindung zum Pico – Port ggf. anpassen!
ser = serial.Serial('COM3', 115200, timeout=1)

# Datenpuffer
voltages, currents, temps, hums = [], [], [], []

def update(frame):
    line = ser.readline().decode('utf-8').strip()
    try:
        voltage, current, temp, hum = map(float, line.split(','))

        # → Konsolenausgabe
        print(f"Spannung: {voltage:.2f} V | Strom: {current:.2f} mA | Temperatur: {temp:.2f} °C | Luftfeuchte: {hum:.2f} %")

        # → Plot-Daten aktualisieren
        voltages.append(voltage)
        currents.append(current)
        temps.append(temp)
        hums.append(hum)

        if len(voltages) > 100:
            voltages.pop(0)
            currents.pop(0)
            temps.pop(0)
            hums.pop(0)

        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(voltages, label="Spannung (V)")
        plt.plot(currents, label="Strom (mA)")
        plt.legend(loc="upper right")

        plt.subplot(2, 1, 2)
        plt.plot(temps, label="Temperatur (°C)")
        plt.plot(hums, label="Luftfeuchte (%)")
        plt.legend(loc="upper right")

    except ValueError:
        pass  # Fehlerhafte Zeile ignorieren

ani = FuncAnimation(plt.gcf(), update, interval=1000)
plt.tight_layout()
plt.show()

