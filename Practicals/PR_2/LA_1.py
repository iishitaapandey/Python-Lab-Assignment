v = float(input("Enter voltage (V): "))
r = float(input("Enter resistance (R): "))

i = v / r

print("\nCurrent:", i)

if i < 0.5:
    print("Low current")
elif i <= 2:
    print("Normal current")
else:
    print("High current")