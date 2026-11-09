
import math


# Calculate parcel delivery charge
def calculate_charge(weight_kg, distance_km, multiplier=1.0):
    basic_charge = (weight_kg * 40) + (distance_km * 1.50)
    return basic_charge * multiplier


# Classify parcel according to weight
def classify_weight(weight_kg):
    if weight_kg <= 2:
        return "Light"
    elif weight_kg <= 5:
        return "Medium"
    else:
        return "Heavy"


# Estimate delivery time
def estimate_delivery_time(distance_km, average_speed=40):
    delivery_hours = distance_km / average_speed
    return math.ceil(delivery_hours)


# Calculate total charge and average distance
def calculate_summary(parcel_records):
    total_amount = 0
    total_distance = 0

    for parcel in parcel_records:
        total_amount += parcel.calculate_charge()
        total_distance += parcel.distance_km

    if len(parcel_records) > 0:
        average_distance = total_distance / len(parcel_records)
    else:
        average_distance = 0

    return total_amount, average_distance


# Sort parcels by delivery distance
def sort_by_distance(parcel_records):
    return sorted(
        parcel_records,
        key=lambda parcel: parcel.distance_km
    )


# Append a parcel record to the text file
def save_record(parcel):
    with open("parcel_records.txt", "a") as file:
        record = (
            f"{parcel.parcel_id} | "
            f"{parcel.receiver_name} | "
            f"{parcel.weight_kg} kg | "
            f"{parcel.distance_km} km | "
            f"{parcel.service_type} | "
            f"Rs. {parcel.calculate_charge():.2f}\n"
        )

        file.write(record)


# Read saved parcel records
def read_records():
    with open("parcel_records.txt", "r") as file:
        records = file.readlines()

    return records
