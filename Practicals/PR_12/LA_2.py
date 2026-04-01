import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print(df[df['Department'] == 'Automotive'])

# b) Details using Employee ID
emp_id = int(input("Enter Employee ID: "))
print(df[df['Employee ID'] == emp_id])

# c) Developers list
print(df[df['Designation'] == 'Developer'])