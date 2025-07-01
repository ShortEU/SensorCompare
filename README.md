SensorCompare

SensorCompare is a modular tool for acquiring, comparing, and visualizing sensor data using a Raspberry Pi Pico microcontroller and Python scripts on a PC.

🚀 Features

Collects data from sensors (AHT10, AHT20, INA219, etc.) via Raspberry Pi Pico

PC-side scripts for automated data logging, sensor comparison, and live plotting

Easy sensor benchmarking and CSV data export

📦 Project Structure

SensorCompare/
├── sensor_plot_pc/        # PC-side Python scripts for data handling and plotting
├── sensor_vergleich/      # Pico-side scripts for sensor communication and control
├── .gitignore
├── README.md
└── SensorCompare.code-workspace

🛠️ Getting Started

1. Clone the repository

git clone https://github.com/ShortEU/SensorCompare.git
cd SensorCompare

2. Set up your Python environments

For each subproject, install dependencies:

PC-side (Data Handling & Plotting)

cd sensor_plot_pc
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Microcontroller-side (Sensor Acquisition)

cd ../sensor_vergleich
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

🕹️ Usage

Flash the Raspberry Pi Pico with your .uf2 firmware as described in the Pico documentation.

Use the PC scripts to collect, plot, and analyze sensor data.

See each subfolder's README for details.

🧰 Requirements

Raspberry Pi Pico

Supported sensors: AHT10, AHT20, AHT30, INA219, etc.

Python 3.8+

pip

📁 Data & Privacy

Sensor data files (.csv) are not tracked by git (see .gitignore).

Firmware files (.uf2) are not tracked by git;

📄 License

This project is private and not licensed for public distribution.

👤 Author

Erwin Schellenberg / ShortEU on GitHub

Test push from new account
