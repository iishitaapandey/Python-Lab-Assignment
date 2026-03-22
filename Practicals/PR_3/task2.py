for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
print()

for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("#", end="")
    print()
print()

word = "python"
for i in range(len(word)):
    for j in range(i+1):
        print(word[i], end="")
    print()
print()

word = "python"
for i in range(1, len(word)+1):
    print(word[:i])