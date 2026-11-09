
# Smart Parcel Dispatch and Delivery Tracker
# Milestone 3: Inheritance and Polymorphism

# Base class
class Parcel:

    # Class variable
    company_name = "Smart Parcel Services"

    # Constructor
    def __init__(self, parcel_id, receiver_name, weight_kg, distance_km):
        self.parcel_id = parcel_id
        self.receiver_name = receiver_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    # Method to calculate standard delivery charge
    def calculate_charge(self):
        charge = (self.weight_kg * 40) + (self.distance_km * 1.50)
        return charge

    # Method to display parcel details
    def display_details(self):
        print("\nCompany Name:", self.company_name)
        print("Parcel ID:", self.parcel_id)
        print("Receiver Name:", self.receiver_name)
        print("Weight:", self.weight_kg, "kg")
        print("Distance:", self.distance_km, "km")
        print("Delivery Charge: Rs.", format(self.calculate_charge(), ".2f"))

    # String representation of parcel
    def __str__(self):
        return f"Parcel {self.parcel_id} - Receiver: {self.receiver_name}"


# Derived class
class ExpressParcel(Parcel):

    # Overriding calculate_charge() method
    def calculate_charge(self):
        basic_charge = super().calculate_charge()
        express_charge = basic_charge * 1.25
        return express_charge

# Creating one standard parcel object
parcel1 = Parcel("PKG101", "Neha", 2.5, 120)

# Creating one express parcel object
parcel2 = ExpressParcel("PKG102", "Rahul", 2.5, 120)


# Displaying standard parcel details
print("========== STANDARD PARCEL ==========")
parcel1.display_details()
print(parcel1)

# Displaying express parcel details
print("\n========== EXPRESS PARCEL ==========")
parcel2.display_details()
print(parcel2)


# Demonstrating polymorphism
print("\n========== POLYMORPHISM ==========")

parcels = [parcel1, parcel2]

for parcel in parcels:
    print(parcel.parcel_id, "Charge: Rs.",
          format(parcel.calculate_charge(), ".2f"))
