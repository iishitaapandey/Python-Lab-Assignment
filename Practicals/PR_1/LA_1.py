name = input("Enter name: ")
emp_id = input("Enter employee ID: ")
dept = input("Enter department: ")
basic = float(input("Enter basic salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

gross = basic + da + hra + ta
net = gross - lic

print("\n--- Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", dept)
print("Basic Salary:", basic)
print("Net Salary:", net)