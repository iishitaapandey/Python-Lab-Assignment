s = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lower = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch == " ":
        spaces += 1
    elif ch.isalpha():
        consonants += 1
    
    if ch.islower():
        lower += 1

print("\nVowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Lowercase letters:", lower)