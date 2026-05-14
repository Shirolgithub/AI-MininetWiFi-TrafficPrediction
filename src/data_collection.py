import csv
import random
import time
from datetime import datetime


CSV_FILE = "data/mobile_network_traffic.csv"


def generate_network_data():

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    station_id = f"sta{random.randint(1,10)}"

    traffic_load = round(random.uniform(5, 100), 2)

    latency = round(random.uniform(1, 20), 2)

    packet_loss = round(random.uniform(0, 5), 2)

    signal_strength = round(random.uniform(-90, -30), 2)

    bandwidth_utilization = round(random.uniform(10, 100), 2)

    active_users = random.randint(1, 50)

    return [
        timestamp,
        station_id,
        traffic_load,
        latency,
        packet_loss,
        signal_strength,
        bandwidth_utilization,
        active_users
    ]


def create_csv():

    header = [
        "Timestamp",
        "Station_ID",
        "Traffic_Load_Mbps",
        "Latency_ms",
        "Packet_Loss_%",
        "Signal_Strength_dBm",
        "Bandwidth_Utilization_%",
        "Active_Users"
    ]

    with open(CSV_FILE, mode='w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(header)


def collect_data():

    create_csv()

    print("\nStarting Real-Time Data Collection...\n")

    while True:

        data = generate_network_data()

        with open(CSV_FILE, mode='a', newline='') as file:

            writer = csv.writer(file)

            writer.writerow(data)

        print("Collected:", data)

        time.sleep(2)


if __name__ == "__main__":

    collect_data()

