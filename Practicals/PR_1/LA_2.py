name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0

print("\nEnter monthly purchases:")
for i in range(1, 13):
    amt = float(input("Month " + str(i) + ": "))
    total = total + amt

print("\n--- Vendor Details ---")
print("Name:", name)
print("Year:", year)
print("Contact:", contact)
print("Email:", email)
print("Annual Purchase:", total)