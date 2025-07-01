import matplotlib.pyplot as plt
import csv
import os
from tkinter import Tk, filedialog

# === Datei mit Dateiauswahldialog auswählen ===
root = Tk()
root.withdraw()  # Fenster ausblenden
filepath = filedialog.askopenfilename(
    title="Wähle eine CSV-Datei",
    filetypes=[("CSV-Dateien", "*.csv")],
    initialdir="SensorTest"
)

if not filepath:
    print("Keine Datei ausgewählt.")
    exit()

print(f"Lade Datei: {filepath}")

# === Daten aus CSV laden ===
zeit, spannung, strom, temperatur, luftfeuchte = [], [], [], [], []

with open(filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        zeit.append(float(row["Zeit (s)"]))
        spannung.append(float(row["Spannung (V)"]))
        strom.append(float(row["Strom (mA)"]))
        temperatur.append(float(row["Temperatur (°C)"]))
        luftfeuchte.append(float(row["Luftfeuchte (%)"]))

# === Plotten ===
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Sensor-Messwerte aus CSV", fontsize=16)

axs[0, 0].plot(zeit, spannung, label="Spannung (V)", color="blue")
axs[0, 0].set_title("Spannung")
axs[0, 0].set_ylabel("V")

axs[0, 1].plot(zeit, strom, label="Strom (mA)", color="red")
axs[0, 1].set_title("Strom")
axs[0, 1].set_ylabel("mA")

axs[1, 0].plot(zeit, temperatur, label="Temperatur (°C)", color="green")
axs[1, 0].set_title("Temperatur")
axs[1, 0].set_ylabel("°C")

axs[1, 1].plot(zeit, luftfeuchte, label="Luftfeuchte (%)", color="orange")
axs[1, 1].set_title("Luftfeuchte")
axs[1, 1].set_ylabel("%")

for ax in axs.flat:
    ax.set_xlabel("Zeit (s)")
    ax.grid(True)

plt.tight_layout()
plt.show()
