import csv
import statistics
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# === Funktion zur Auswahl von Dateien ===
def choose_files():
    Tk().withdraw()  # Verhindert, dass ein leeres Tk-Fenster angezeigt wird
    files = {}
    print("Bitte wählen Sie die CSV-Datei für AHT10 aus:")
    files["AHT10"] = askopenfilename(filetypes=[("CSV-Dateien", "*.csv")])
    print("Bitte wählen Sie die CSV-Datei für AHT20 aus:")
    files["AHT20"] = askopenfilename(filetypes=[("CSV-Dateien", "*.csv")])
    print("Bitte wählen Sie die CSV-Datei für AHT30 aus:")
    files["AHT30"] = askopenfilename(filetypes=[("CSV-Dateien", "*.csv")])
    return files

# === CSV-Dateien auswählen ===
csv_files = choose_files()

# === Daten laden ===
daten = {}

for sensor_name, filepath in csv_files.items():
    zeit, temp, feuchte, strom = [], [], [], []

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            zeit.append(float(row["Zeit (s)"]))
            temp.append(float(row["Temperatur (°C)"]))
            feuchte.append(float(row["Luftfeuchte (%)"]))
            strom.append(float(row["Strom (mA)"]))

    daten[sensor_name] = {
        "zeit": zeit,
        "temp": temp,
        "feuchte": feuchte,
        "strom": strom,
    }

# === Diagramm-Funktion ===
def plot_messwerte(daten, key, ylabel, title):
    plt.figure(figsize=(10, 6))
    for name, werte in daten.items():
        plt.plot(werte["zeit"], werte[key], label=name)
    plt.xlabel("Zeit (s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === Plot: Temperatur, Feuchte, Stromverbrauch ===
plot_messwerte(daten, "temp", "Temperatur (°C)", "Temperaturvergleich")
plot_messwerte(daten, "feuchte", "Luftfeuchte (%)", "Luftfeuchtevergleich")
plot_messwerte(daten, "strom", "Strom (mA)", "Stromverbrauchsvergleich")

# === Statistische Auswertung ===
def auswertung(name, werte):
    def stats(data):
        return {
            "min": min(data),
            "max": max(data),
            "mean": statistics.mean(data),
            "stdev": statistics.stdev(data) if len(data) > 1 else 0
        }

    print(f"\n Sensor: {name}")
    print("Temperatur:")
    for k, v in stats(werte["temp"]).items():
        print(f"  {k}: {v:.2f}")
    print("Luftfeuchte:")
    for k, v in stats(werte["feuchte"]).items():
        print(f"  {k}: {v:.2f}")
    print("Strom:")
    for k, v in stats(werte["strom"]).items():
        print(f"  {k}: {v:.2f}")

# === Ausgabe pro Sensor ===
print("\n=== Statistische Auswertung ===")
for sensor_name, werte in daten.items():
    auswertung(sensor_name, werte)