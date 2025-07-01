import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        self.timestamps = []
        self.voltages = []
        self.currents = []
        self.temperatures = []
        self.humidities = []

        plt.ion()
        self.fig, self.axs = plt.subplots(2, 1, figsize=(10, 8))

    def update(self, t, voltage, current, temperature, humidity):
        self.timestamps.append(t)
        self.voltages.append(voltage)
        self.currents.append(current)
        self.temperatures.append(temperature)
        self.humidities.append(humidity)

        max_len = 100
        if len(self.timestamps) > max_len:
            self.timestamps = self.timestamps[-max_len:]
            self.voltages = self.voltages[-max_len:]
            self.currents = self.currents[-max_len:]
            self.temperatures = self.temperatures[-max_len:]
            self.humidities = self.humidities[-max_len:]

        self.axs[0].clear()
        self.axs[0].plot(self.timestamps, self.voltages, label='Spannung [V]')
        self.axs[0].plot(self.timestamps, self.currents, label='Strom [mA]')
        self.axs[0].legend()
        self.axs[0].set_title('Elektrische Messwerte')

        self.axs[1].clear()
        self.axs[1].plot(self.timestamps, self.temperatures, label='Temperatur [°C]')
        self.axs[1].plot(self.timestamps, self.humidities, label='Luftfeuchte [%]')
        self.axs[1].legend()
        self.axs[1].set_title('Umweltwerte')

        plt.pause(0.5)

    def close(self):
        plt.ioff()
        plt.show()
