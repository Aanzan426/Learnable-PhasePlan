# Problem Statement: Global Sustainability Monitoring and Optimization System

# Initial File Handler
def initial (filename):
    with open (filename, "w+") as z:
        if z.tell() == 0:
            z.write("*** Global Report ***\n")
            with open ("energy_report.txt", "w+") as a:
                a.write("*** Energy Report ***\n")
            with open ("emission_report.txt", "w+") as b:
                b.write("*** Emission Report ***\n")
            with open ("water_report.txt", "w+") as c:
                c.write("*** Water Report ***\n")
            with open ("aqi_report.txt", "w+") as d:
                d.write("*** AQI Report ***\n")
            with open ("waste_report.txt", "w+") as e:
                e.write("*** Waste Report ***\n")
            with open ("climate_report.txt", "w+") as f:
                f.write("*** Climate Report ***\n")
            with open ("transport_report.txt", "w+") as g:
                g.write("*** Transport Report ***\n")
            with open ("datacenter_report.txt", "w+") as h:
                h.write("*** Datacenter Report ***\n")



# Energy Analytics
electricity_consumption = {
    "Building_A": [120, 135, 150, 160, 145, 130, 125, 140],
    "Building_B": [95, 100, 110, 120, 115, 105, 98, 102],
    "Building_C": [200, 210, 220, 230, 225, 215, 205, 210]
}

def building_classification (parameter):
    report_lines = []
    for item, values in parameter.items():
        res = calculate_avg (values)
        resnec = calculate_growth_rate (res, len(values))
        line = (f"Power consumption of {item} is {sum(values)}: Average {res} kWH, Growth Rate of {resnec} kWH")
        print(line)
        report_lines.append(line)
    return "\n".join(report_lines)

def calculate_avg (data):
    try:
        average = sum(data) / len(data)
        return average
    except ZeroDivisionError:
        print("Couldnt calcualte Average. Try Again.")

def calculate_growth_rate(data, num):
    return data / num


class Energy_Source:
    def __init__(self, power_output, capacity):
        self.power_output = power_output
        self._capacity = capacity
    def generate_power(self):
        return self.power_output * self._capacity

class Solar(Energy_Source):
    def __init__(self, power_output, capacity, time_taken):
        super().__init__(power_output, capacity)
        self.__time_taken = time_taken
    def time_to_generate_power(self):
        return super().generate_power() // self.__time_taken

class Wind(Energy_Source):
    def __init__(self, power_output, capacity, wind_speed):
        super().__init__(power_output, capacity)
        self._wind_speed = wind_speed
    def rotations(self):
        return self._capacity // self._wind_speed

class Hydro(Energy_Source):
    def __init__(self, power_output, capacity, water_level):
        super().__init__(power_output, capacity)
        self.water_level = water_level
    def mass_of_water(self):
        height = self.water_level
        density = 1000  # kg/m^3
        return density * (height ** 3)




#Emission Compliance
co2_emissions = {
    "Factory_1": 1200,
    "Factory_2": 950,
    "Factory_3": 1800,
    "Factory_4": 760
}

def factory_classification (parameter):
    try:
        total = 0
        num = 0
        report_lines = []
        for item, value in parameter.items():
            try:
                if value > 1000:
                    line = (f"{item} is Classified under: Compliant catgory ({value} tonnes)")
                else:
                    line = (f"{item} is Classified under: Non-Compliant catgory ({value} tonnes)")
                total += value
                num += 1
            except ValueError:
                print("Invalid Input Type. Try Again.")
        print(line)
        report_lines.append(line)
        avg = total / num
        res = calculate_growth_rate(avg, num)

        summary = (f"Overall Factory Average Emission is {res:.2f} tonnes")
        print(summary)

        report_lines.append(summary)
        return "\n".join(report_lines)
    except KeyError:
        print("Factory Data Missing. Try Again.")





# Water Monitoring
water_consumption = [
    {"zone": "North", "liters": 50000},
    {"zone": "South", "liters": 42000},
    {"zone": "East", "liters": 61000},
    {"zone": "West", "liters": 47000}
]

def water_monitoring(parameter):
    try:
        with open("water_report.txt", "r+") as c:
            for item in parameter:
                if item["liters"] > 49000:
                    print(f"Zone {item['zone']} is above conservation level...Deploy ALERTS!!!")
                    c.write(f"Zone {item['zone']} expended {item['liters']} litres of water => Above Critical Level\n")
                elif item["liters"] < 49000:
                    print(f"Zone {item['zone']} is within conservation level.")
                    c.write(f"Zone {item['zone']} expended {item['liters']} litres of water => Within Permissible Level\n")
                else:
                    pass
            c.write("\n")
        return "Water monitoring completed."
    except FileNotFoundError:
        print("File water_report.txt not found. Try Again.")
        return None





# AQI Alerts
aqi_values = {
    "City_X": [85, 90, 95, 100, 110, 120],
    "City_Y": [70, 75, 80, 85, 90, 95],
    "City_Z": [150, 160, 170, 180, 190, 200]
}

def aqi_alerts(parameter):
    report_lines = []
    with open ("aqi_report.txt", "r+") as d:
        for item, values in parameter.items():
            try:
                avg = sum(values) // len(values)
            except ValueError(values):
                print("Values not in right format. Try Again.")

            if avg >= 50 and avg < 75:
                line = (f"The AQI for {item} is {avg}... Audited Result: Good")
                d.write(f"Air Quality Advisories: {item}: {avg}: GOOD" + "\n")

            elif avg >= 75 and avg < 100:
                line = (f"The AQI for {item} is {avg}... Audited Result: Moderate")
                d.write(f"Air Quality Advisories: {item}: {avg}: MODERATE" + "\n")

            elif avg >= 100 and avg < 125:
                line = (f"The AQI for {item} is {avg}... Audited Result: Poor")
                d.write(f"Air Quality Advisories: {item}: {avg}: POOR" + "\n")

            elif avg >= 125 and avg <= 175:
                line = (f"The AQI for {item} is {avg}... Audited Result: Hazardous")
                d.write(f"Air Quality Advisories: {item}: {avg}: HAZARDOUS" + "\n")

            else:
                continue
            print(line)
            report_lines.append(line)

        d.write("\n")
    return "\n".join(report_lines)





# Waste Segregation
waste_items = [
    ("Organic", 120),
    ("Recyclable", 80),
    ("Hazardous", 40),
    ("Organic", 95),
    ("Recyclable", 60)
]

class WasteType:
    def __init__(self, quantity, toxicity):
        self._quantity = quantity
        self._toxicity = toxicity
    def process_waste(self):
        return self._quantity * self._toxicity

class Organic(WasteType):
    def process_waste(self):
        return f"[Organic] Composted {self._quantity} kg (Toxicity {self._toxicity})"

class Recyclable(WasteType):
    def process_waste(self):
        return f"[Recyclable] Recycled {self._quantity} kg with efficiency (Toxicity {self._toxicity})"

class Hazardous(WasteType):
    def process_waste(self):
         return f"[Hazardous] Disposed {self._quantity} kg with safety cost (Toxicity {self._toxicity})"





# Climate Data Cleaning
climate_data = [
    {"day": "Mon", "temperature": 28, "rainfall": 5},
    {"day": "Tue", "temperature": 30, "rainfall": 0},
    {"day": "Wed", "temperature": 27, "rainfall": 12},
    {"day": "Thu", "temperature": 25, "rainfall": 20},
    {"day": "Fri", "temperature": 29, "rainfall": 2}
]

def summarize_climate(data):
    anomalies = []
    valid_entries = []
    for d in data:
        try:
            temp = int(d["temperature"])
            rain = int(d["rainfall"])
            if temp < -50 or temp > 60 or rain < 0:
                raise ValueError(f"Invalid sensor reading for {d['day']}")
            valid_entries.append({"day": d["day"], "temperature": temp, "rainfall": rain})
        except (ValueError, TypeError):
            anomalies.append(f"[ERROR] Invalid sensor input for {d['day']} → Skipped")

    if valid_entries:
        avg_temp = sum(d["temperature"] for d in valid_entries) / len(valid_entries)
        avg_rain = sum(d["rainfall"] for d in valid_entries) / len(valid_entries)
        for d in valid_entries:
            if d["temperature"] > avg_temp + 2:
                anomalies.append(f"{d['day']} unusually hot ({d['temperature']}°C)")
            elif d["temperature"] < avg_temp - 2:
                anomalies.append(f"{d['day']} unusually cold ({d['temperature']}°C)")
            if d["rainfall"] > avg_rain * 2:
                anomalies.append(f"{d['day']} heavy rainfall ({d['rainfall']} mm)")
            elif d["rainfall"] == 0:
                anomalies.append(f"{d['day']} no rainfall")

    with open("climate_report.txt", "r+") as f:
        for entry in data:
            f.write(f"{entry['day']}: Temp={entry['temperature']}°C, Rain={entry['rainfall']}mm\n")
        f.write("\nAnomalies:\n")
        for a in anomalies:
            f.write(f"- {a}\n")

    for entry in data:
        print(f"{entry['day']}: Temp={entry['temperature']}°C, Rain={entry['rainfall']}mm")
    print("\nAnomalies:")
    for a in anomalies:
        print("- ", a)

    return anomalies





# Transport Optimization
transport_data = [
    {"vehicle": "Car", "fuel": "Petrol", "distance": 120, "emission": 180},
    {"vehicle": "Bus", "fuel": "Diesel", "distance": 300, "emission": 90},
    {"vehicle": "Bike", "fuel": "Petrol", "distance": 60, "emission": 40},
]

class Vehicle:
    def __init__(self, emission, capacity):
        self._emission = emission
        self._capacity = capacity
    def calculate_fuel_efficiency(self, distance):
        try:
            return distance / self._emission
        except ZeroDivisionError:
            return float("inf")
    def carbon_footprint (self, distance):
        try:
            return self._emission * (distance / 100)
        except ZeroDivisionError:
            return 0.0

class Car(Vehicle):
    def calculate_fuel_efficiency(self, distance):
        try:
            return (distance / self._emission) * 2  # factor for cars
        except ZeroDivisionError:
            return float("inf")

class Bus(Vehicle):
    def calculate_fuel_efficiency(self, distance):
        try:
            return (distance / self._emission) * 0.5  # shared load
        except ZeroDivisionError:
            return float("inf")

class Bike(Vehicle):
    def calculate_fuel_efficiency(self, distance):
        try:
           return (distance / self._emission) * 0.2  # minimal emission
        except ZeroDivisionError:
            return float("inf")




# Data Center Load Management
server_load = {
    "DataCenter_1": [65, 70, 75, 80, 85],
    "DataCenter_2": [50, 55, 60, 65, 70],
    "DataCenter_3": [90, 92, 95, 97, 99]
}

def energy_savings (load):
    report_lines = []
    try:
        with open ("datacenter_report.txt", "r+") as h:
            for data, values in load.items():
                avg = sum(values) / len(values)
                if avg >= 72:
                    line = f"{data}: Average Load {avg:.2f}% → Switch to Power Saving Mode"
                else:
                    line = f"{data}: Average Load {avg:.2f}% → Stay in High Performance Mode"
                print(line)
                report_lines.append(line)
            h.write("\n")
    except FileNotFoundError:
        return "File Not Found. Try Again."
    return "\n".join(report_lines)





# Global Sustainability Report
def generate_global_report(filename):
    try:
        files = [
            "energy_report.txt",
            "emission_report.txt",
            "water_report.txt",
            "aqi_report.txt",
            "waste_report.txt",
            "climate_report.txt",
            "transport_report.txt",
            "datacenter_report.txt"
        ]

        category_count = {"High": 0, "Moderate": 0, "Low": 0}
        anomalies = []
        performers = []

        with open(filename, "w+") as global_file:
            global_file.write("=== Global Sustainability Report ===\n\n")

            for f in files:
                try:
                    with open(f, "r") as domain_file:
                        content = domain_file.read()
                        global_file.write(f"\n--- {f.replace('_report.txt','').title()} ---\n")
                        global_file.write(content + "\n")

                        if "HIGH" in content.upper():
                            category_count["High"] += 1
                        if "MODERATE" in content.upper():
                            category_count["Moderate"] += 1
                        if "LOW" in content.upper() or "HAZARDOUS" in content.upper():
                            category_count["Low"] += 1
                        if "ERROR" in content.upper() or "ALERT" in content.upper():
                            anomalies.append(f"Check anomalies in {f}")

                        performers.append((f, len(content)))
                except FileNotFoundError:
                    global_file.write(f"[WARNING] {f} not found.\n")

            top3 = sorted(performers, key=lambda x: x[1], reverse=True)[:3]

            global_file.write("\n=== Composite Summary ===\n")
            global_file.write(f"High Performance Entities: {category_count['High']}\n")
            global_file.write(f"Moderate Performance Entities: {category_count['Moderate']}\n")
            global_file.write(f"Low Performance Entities: {category_count['Low']}\n")

            global_file.write("\nTop 3 Sustainable Performers:\n")
            for p in top3:
                global_file.write(f"- {p[0]} (score proxy {p[1]})\n")

            global_file.write("\nAnomalies:\n")
            if anomalies:
                for a in anomalies:
                    global_file.write(f"⚠ {a}\n")
            else:
                global_file.write("No anomalies detected.\n")

            global_file.write("\nRecommendations:\n")
            if category_count["Low"] > 0:
                global_file.write("⚠ Strengthen policies in low-performing domains.\n")
            if category_count["Moderate"] > category_count["High"]:
                global_file.write("⚠ Invest more in moderate performers to push them into high category.\n")
            if not anomalies and category_count["Low"] == 0:
                global_file.write("✅ Overall sustainability performance is strong.\n")

        return "Global Sustainability Report generated successfully."

    except Exception as e:
        return f"Unexpected error occurred: {e}"
    finally:
        print("Global report generation process completed.")





def main():
    initial("global_report.txt")
    while True:
        print("""Menu:
            1. Energy Analytics
            2. Emission Compliance
            3. Water Monitoring
            4. AQI Alerts
            5. Waste Segregation
            6. Climate Data Cleaning
            7. Transport Optimization
            8. Data Center Load Management
            9. Generate Global Sustainability Report
        """)
        n = int(input("Enter Choice: "))

        if n == 1:
            try:
                power = int(input("Enter Power Output Value (MWs): "))
                cap = int(input("Enter Capacity Value (Tonnes): "))
                time = int(input("Enter Time (Hrs): "))
                speed = int(input("Enter Wind Speed (Kts): "))
                level = int(input("Enter Water Level (Mtrs): "))

                solar_erg = Solar(power_output=power, capacity=cap, time_taken=time)
                wind_erg = Wind(power_output=power, capacity=cap, wind_speed=speed)
                hydro_erg = Hydro(power_output=power, capacity=cap, water_level=level)
                building_dep = building_classification (electricity_consumption)

                with open("energy_report.txt", "a") as a:
                    a.write(f"Power generated per hour => {solar_erg.time_to_generate_power()}\n")
                    a.write(f"One Unit of Wind => {wind_erg.rotations()}\n")
                    a.write(f"Mass of Total Volume of Water => {hydro_erg.mass_of_water()}\n\n")
                    a.write(f"Building Electricity Consumption: {building_dep}")

            except FileNotFoundError():
                print("Filename energy_report.txt not found. Try Again.")


        elif n == 2:
            result = factory_classification(co2_emissions)
            print("CO2 Emission Report:", result)
            with open ("emission_report.txt", "r+") as b:
                b.write(result + "\n")

        elif n == 3:
            result = water_monitoring(water_consumption)
            print("Water Consumption Data:", result)


        elif n == 4:
            result = aqi_alerts(aqi_values)
            print(f"Air Quality Index: {result}")


        elif n == 5:
            with open("waste_report.txt", "a") as e:
                for data in waste_items:
                    try:
                        tox = int(input(f"Enter Toxicity Level (1 to 10) for {data[0]} ({data[1]} kg): "))
                        if data[0] == "Organic":
                            obj = Organic(quantity=data[1], toxicity=tox)
                            line = obj.process_waste()
                        elif data[0] == "Recyclable":
                            obj = Recyclable(quantity=data[1], toxicity=tox)
                            line = obj.process_waste()
                        elif data[0] == "Hazardous":
                            obj = Hazardous(quantity=data[1], toxicity=tox)
                            line = obj.process_waste()
                        else:
                           raise KeyError(f"Waste type '{data[0]}' not recognized")
                        e.write(line + "\n")
                        print("✔", line)
                    except KeyError as ke:
                        error_msg = f"[ERROR] {ke} → Skipping {data[1]} kg"
                        e.write(error_msg + "\n")
                        print(error_msg)
                e.write("\n")


        elif n == 6:
            result = summarize_climate(climate_data)
            print(f"Clean Climate Data: {result}")

        elif n == 7:
            car_data = next(item for item in transport_data if item["vehicle"] == "Car")
            bus_data = next(item for item in transport_data if item['vehicle'] == "Bus")
            bike_data = next(item for item in transport_data if item["vehicle"] == "Bike")

            car_cap = int(input("Enter Capacity Value (Litres - Car): "))
            bus_cap = int(input("Enter Capacity Value (Litres - Bus): "))
            bike_cap = int(input("Enter Capacity Value (Litres - Bike): "))

            car = Car(emission = car_data['emission'], capacity = car_cap)
            bus = Bus(emission = bus_data['emission'], capacity = bus_cap)
            bike = Bike(emission = bike_data['emission'], capacity = bike_cap)

            results = {
                "Car": {
                    "efficiency": car.calculate_fuel_efficiency(car_data["distance"]),
                    "footprint": car.carbon_footprint(car_data["distance"])
                },
                "Bus": {
                    "efficiency": bus.calculate_fuel_efficiency(bus_data["distance"]),
                    "footprint": bus.carbon_footprint(bus_data["distance"])
                },
                "Bike": {
                    "efficiency": bike.calculate_fuel_efficiency(bike_data["distance"]),
                    "footprint": bike.carbon_footprint(bike_data["distance"])
                }
            }

            ranked = sorted(results.items(), key=lambda x: x[1]["footprint"])

            with open ("transport_report.txt", "r+") as g:
                for vehicle, metrics in ranked:
                    g.write(f"{vehicle:<6} | Fuel Efficiency: {metrics['efficiency']:.2f} | Carbon Footprint: {metrics['footprint']:.2f}\n")
            for vehicle, metrics in ranked:
                print(f"{vehicle:<6} | Fuel Efficiency: {metrics['efficiency']:.2f} | Carbon Footprint: {metrics['footprint']:.2f}\n")


        elif n == 8:
            result = energy_savings (server_load)
            print("\nData Center Optimization Summary:\n")
            print(result)

        elif n == 9:
            result = generate_global_report("global_report.txt")
            print(result)
        
        else:
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
