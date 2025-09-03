# Simple Shared Bill Splitter

print("=== Shared Bill Splitter ===")

# 1. Take inputs
rent = float(input("1) Enter hostel/flat rent: "))
food = float(input("2) Enter total food/snacks amount: "))
electricity_units = float(input("3) Enter electricity units used: "))
charge_per_unit = float(input("4) Enter charge per electricity unit: "))
persons = int(input("5) Enter number of persons: "))

# 2. Calculate electricity bill
electricity_bill = electricity_units * charge_per_unit

# 3. Total bill
total_bill = rent + food + electricity_bill

# 4. Per person share
per_person = total_bill / persons

# 5. Display results
print("\n--- Bill Breakdown ---")
print("Rent:              ", rent)
print("Food/Snacks:       ", food)
print("Electricity Bill:  ", electricity_bill)
print("Total Bill:        ", total_bill)

print("\n--- Split ---")
print("Each person will pay:", round(per_person, 2))
