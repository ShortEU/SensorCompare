# SensorVergleich – Spannungs-, Strom- und Umweltdaten erfassen & auswerten

Dieses Projekt liest Daten von INA219 und AHT10 Sensoren auf einem Raspberry Pi Pico aus, überträgt sie per serieller Schnittstelle an den PC und speichert sie dort in einer CSV-Datei zur späteren grafischen Auswertung.

---

## Projektstruktur

```
_sensorVergleich/     → Code für Raspberry Pi Pico
_sensorPlotPC/        → Python-Skripte für Datenerfassung & Plotten
  └─ SensorTest/      → Hier werden CSV-Dateien automatisch abgelegt
```

---

## Teil 1: PC-Vorbereitung

### 1. Virtuelle Umgebung einrichten (nur beim ersten Mal)

```bash
cd _sensorPlotPC
python -m venv venv
source venv/Scripts/activate  # Bei Windows mit Git Bash
pip install -r requirements.txt  # Falls vorhanden
Python Interpreter auswählen

# oder manuell:
pip install matplotlib pyserial
```

---

## Teil 2: Microcontroller starten

### 1. Öffne `main.py` aus `_sensorVergleich/` mit Pymakr.  
### 2. Verbinde den Raspberry Pi Pico (USB).
### 3. Starte das Skript auf dem Mikrocontroller.

> Das Skript sendet alle 5 Sekunden CSV-formatierte Daten wie:
> `3.28,102.53,24.51,49.34`

---

## Teil 3: Testdaten erfassen (vom PC aus)

### 1. Starte das Datensammel-Skript:

```bash
python datenfasser.py
```

Die Daten werden gespeichert in:  
`_sensorPlotPC/SensorTest/test_YYYY-MM-DD_HH-MM-SS.csv`

---

## Teil 4: Live-Plot (optional)

### Starte den Plot während oder nach der Messung:

```bash
python live_plot.py
```

Zeigt einen Live-Plot der eingehenden Sensorwerte von `COM3`.  
Stelle sicher, dass kein anderes Skript (`datenfasser.py`, Pymakr) die serielle Schnittstelle blockiert.

---

## Teil 5: csv-plot (optional)

### Starte csv plot nach dem Erfassen der Daten:

```bash
python csv_plot.py
```
Wähle eine csv aus diese wird mit Matplotlib Grafisch dargestellt.

---

## Teil 6: vergleich-plot

## Starte vergleich plot nach dem Erfassen der Daten:

```bash
python vergleich_plot.py
```

Wählt drei csv Daten aus den Ordnern AHT10,20 und 30 aus und vergleicht die Werte miteinander.
Anschließend werden diese Grafisch dargestellt und können als PNG gespeichert werden

---

## Hinweise

- COM-Port ggf. in `datenfasser.py` und `live_plot.py` anpassen (`COM3`)
- Der Raspberry Pi Pico sendet kontinuierlich – Tests können manuell oder per Zeitbegrenzung beendet werden
- `SensorTest/` wird automatisch erstellt – dort liegen deine .csv-Dateien

---

## To-Do / Ideen

- [ ] GUI für Start/Stopp der Tests
- [ ] Tests mit Metadaten (z. B. Umgebung, Testzweck)
- [ ] Automatische Auswertung nach CSV-Erzeugung

---

Von E.S
