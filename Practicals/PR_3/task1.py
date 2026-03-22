for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
print()

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
print()

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
print()

for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")
    print()
print()

num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
print()

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()