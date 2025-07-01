import serial
import csv
import os
import time
from datetime import datetime
from tkinter import Tk, filedialog

# === Konfiguration ===
PORT = 'COM8'
BAUDRATE = 115200
DAUER_SEKUNDEN = 30  # z. B. 60 Sekunden Testlauf

# === Zielordner auswählen ===
root = Tk()
root.withdraw()  # Kein Tkinter-Fenster anzeigen
output_folder = filedialog.askdirectory(title="Wähle Zielordner für die CSV-Datei")

if not output_folder:
    print("Kein Ordner ausgewählt. Abbruch.")
    exit()

# === Eindeutiger Dateiname ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"test_{timestamp}.csv"
filepath = os.path.join(output_folder, filename)

# === CSV-Datei vorbereiten ===
with open(filepath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Zeit (s)", "Spannung (V)", "Strom (mA)", "Temperatur (°C)", "Luftfeuchte (%)"])

    with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
        print("Starte Messung...")

        start = None  # Startzeit ist zunächst nicht gesetzt
        try:
            while True:
                line = ser.readline().decode().strip()
                if line:
                    print(f"> empfangen: {line}")
                    parts = line.split(",")
                    if len(parts) == 4:
                        try:
                            voltage = float(parts[0])
                            current = float(parts[1])
                            temperature = float(parts[2])
                            humidity = float(parts[3])
                            
                            if start is None:
                                # Startzeit setzen, wenn der erste gültige Wert empfangen wird
                                start = time.time()
                                print("Messung gestartet.")

                            zeit = time.time() - start
                            writer.writerow([round(zeit, 2), voltage, current, temperature, humidity])
                            print(f"{round(zeit,1)}s: V={voltage}V I={current}mA T={temperature}°C H={humidity}%")
                        except ValueError:
                            print("Ungültige Daten – Übersprungen.")

                # Messung stoppen, wenn das Zeitlimit erreicht ist
                if start is not None and DAUER_SEKUNDEN and (time.time() - start) > DAUER_SEKUNDEN:
                    print("Zeitlimit erreicht.")
                    break

        except KeyboardInterrupt:
            print("Messung manuell abgebrochen.")

print(f"Daten gespeichert in: {filepath}")
