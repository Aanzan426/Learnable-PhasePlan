# Global Sustainability Monitoring & Optimization System 🌍

## Overview
This project implements a **Python-based Global Sustainability Monitoring & Optimization System** that integrates multiple sustainability domains:
- Energy
- Emissions
- Water
- Air Quality
- Waste
- Climate Data
- Transportation
- Data Center Efficiency

The system demonstrates **Phase 1 fundamentals** plus advanced **OOP, error handling, analytics, and modular design**.
It produces **domain-specific reports** and a **composite global report** summarizing performance, anomalies, and recommendations.

---

## Features by Domain

### 1. Energy Analytics
- **Dataset:** Hourly electricity consumption (kWh) per building.
- **Classification:** Energy Efficient / Moderate / Intensive.
- **Functions:** `calculate_average(data)`, `calculate_growth_rate(values)`.
- **OOP:** `EnergySource` base class → `Solar`, `Wind`, `Hydro`.
- **Report:** `energy_report.txt`.
- **Exceptions:** `ZeroDivisionError`, `FileNotFoundError`.

### 2. Emission Compliance
- **Dataset:** Annual CO2 emissions per factory.
- **Classification:** Compliant / Non‑Compliant.
- **Functions:** `calculate_growth_rate(values)`.
- **Report:** `emission_report.txt`.
- **Exceptions:** `KeyError`, `ValueError`.

### 3. Water Monitoring
- **Dataset:** Daily water consumption per zone.
- **Classification:** Alerts if water > threshold.
- **Report:** `water_report.txt`.
- **Exceptions:** `FileNotFoundError`, `pass` for incomplete data.

### 4. AQI Alerts
- **Dataset:** Hourly AQI values per city.
- **Classification:** Good / Moderate / Poor / Hazardous.
- **Report:** `aqi_report.txt`.
- **Exceptions:** `ValueError`, skip faulty readings.

### 5. Waste Segregation
- **Dataset:** Waste items (organic, recyclable, hazardous).
- **OOP:** `WasteType` base class → `Organic`, `Recyclable`, `Hazardous`.
- **Report:** `waste_report.txt`.
- **Exceptions:** `KeyError`.

### 6. Climate Data Cleaning
- **Dataset:** Temperature and rainfall.
- **Functions:** `summarize_climate(data)` → anomalies.
- **Report:** `climate_report.txt`.
- **Exceptions:** `ValueError`.

### 7. Transport Optimization
- **Dataset:** Fuel type, distance, emissions.
- **Classification:** Rank vehicles by carbon footprint.
- **Functions:** `carbon_footprint(vehicle)`.
- **OOP:** `Vehicle` base class → `Car`, `Bus`, `Bike`.
- **Report:** `transport_report.txt`.
- **Exceptions:** `ZeroDivisionError`.

### 8. Data Center Load Management
- **Dataset:** Server load data.
- **Classification:** Switch to power‑saving mode if load > threshold.
- **Functions:** `energy_savings(load)`.
- **Report:** `datacenter_report.txt`.
- **Exceptions:** `FileNotFoundError`.

### 9. Global Sustainability Report
- **Report:** `global_report.txt`.
- **Functions:** Summarize all domains, count categories, identify top 3 performers, highlight anomalies, recommend improvements.
- **Exceptions:** Robust closure with `try/except/finally`.

---

## Extended Features 🌶️
- **Menu-driven interface**:
  1. Energy Analytics
  2. Emission Compliance
  3. Water Monitoring
  4. AQI Alerts
  5. Waste Segregation
  6. Climate Data Cleaning
  7. Transport Optimization
  8. Data Center Load Management
  9. Generate Global Sustainability Report
- **Future Twist:** Easily add new sustainability domains (e.g., agriculture, forestry) using OOP + modular functions.

---

## Deliverables
- `sustainability_system.py` → main script.
- Domain-specific report files:
- `energy_report.txt`
- `emission_report.txt`
- `water_report.txt`
- `aqi_report.txt`
- `waste_report.txt`
- `climate_report.txt`
- `transport_report.txt`
- `datacenter_report.txt`
- `global_report.txt` → composite analytics.

---

## Usage
1. Clone or download the project.
2. Run the script:
 ```bash
 python sustainability_system.py

---

## Developed by Deepaansh Deepak Sial
## Global Sustainability Monitoring & Optimization System Project (2025)


