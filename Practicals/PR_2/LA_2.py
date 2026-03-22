h = float(input("Enter hardness: "))
c = float(input("Enter carbon content: "))
t = float(input("Enter tensile strength: "))

cond1 = h > 50
cond2 = c < 0.7
cond3 = t > 5600

count = cond1 + cond2 + cond3

if count == 3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif count == 1:
    grade = 6
else:
    grade = 5

print("\nGrade of steel:", grade)