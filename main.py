from delivery_utils import (
    calculate_charge as get_delivery_charge,
    classify_weight,
    estimate_delivery_time,
    calculate_summary,
    sort_by_distance,
    save_record,
    read_records
)

# Base class
class Parcel:
    company_name = "Smart Parcel Services"

    def __init__(
        self, parcel_id, receiver_name,
        weight_kg, distance_km, service_type="Standard"
    ):
        self.parcel_id = parcel_id
        self.receiver_name = receiver_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km
        self.service_type = service_type

    def calculate_charge(self):
        return get_delivery_charge(
            self.weight_kg,
            self.distance_km
        )

    def display_details(self):
        print("\nParcel ID:", self.parcel_id)
        print("Receiver:", self.receiver_name)
        print("Weight:", self.weight_kg, "kg")
        print("Distance:", self.distance_km, "km")
        print("Service:", self.service_type)
        print("Weight Category:", classify_weight(self.weight_kg))
        print(
            "Delivery Charge: Rs.",
            format(self.calculate_charge(), ".2f")
        )

    def __str__(self):
        return f"Parcel {self.parcel_id} - {self.receiver_name}"

# Child class
class ExpressParcel(Parcel):
    def calculate_charge(self):
        basic_charge = super().calculate_charge()
        return basic_charge * 1.25

# Select the appropriate parcel class
service_classes = {
    "Standard": Parcel,
    "Express": ExpressParcel
}

print("===== SMART PARCEL DISPATCH TRACKER =====")

parcels = []

print("\nAvailable Services: Standard, Express")
print("Enter DONE as Parcel ID to finish dispatch.")

while True:

    parcel_id = input("\nEnter Parcel ID: ").strip()

    if parcel_id.upper() == "DONE":
        break

    receiver_name = input("Enter Receiver Name: ")

    # Handle invalid numeric input
    try:
        weight = float(input("Enter Weight (kg): "))
        distance = float(input("Enter Distance (km): "))

        if weight <= 0 or distance <= 0:
            print("Weight and distance must be positive.")
            print("Please enter the parcel details again.")
            continue

    except ValueError:
        print("Error: Please enter valid numeric values.")
        print("Parcel was not accepted.")
        continue

    service = input("Enter Service Type: ").strip().title()

    # Handle unavailable service
    try:
        parcel_class = service_classes[service]

    except KeyError:
        print("Error: Service is unavailable.")
        print("Please choose Standard or Express.")
        continue

    # Create parcel object
    parcel = parcel_class(
        parcel_id.upper(),
        receiver_name.title(),
        weight,
        distance,
        service
    )

    parcels.append(parcel)

    # Save parcel details in text file
    save_record(parcel)

    print("\nParcel Accepted Successfully!")
    parcel.display_details()

    delivery_time = estimate_delivery_time(
        distance,
        average_speed=40
    )

    print("Estimated Delivery Time:", delivery_time, "hours")


# Dispatch summary
total_amount, average_distance = calculate_summary(parcels)

print("\n========== DISPATCH SUMMARY ==========")
print("Total Valid Parcels:", len(parcels))
print("Total Dispatch Amount: Rs.", format(total_amount, ".2f"))
print("Average Delivery Distance:", format(average_distance, ".2f"), "km")

print("\nParcels Sorted by Distance:")

sorted_parcels = sort_by_distance(parcels)

for parcel in sorted_parcels:
    print(parcel.parcel_id, "-", parcel.distance_km, "km")


# Read and display saved records
print("\n========== SAVED DISPATCH RECORDS ==========")

try:
    records = read_records()

    for record in records:
        print(record, end="")

except FileNotFoundError:
    print("Error: parcel_records.txt was not found.")
    print("No saved dispatch records are available.")

print("============================================")
