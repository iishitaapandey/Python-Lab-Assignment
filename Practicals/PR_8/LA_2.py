src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

f1 = open(src, "r")
f2 = open(dest, "w")

for line in f1:
    line = line.strip()
    
    if line.startswith("#") or line == "":
        continue
    
    f2.write(line + "\n")

f1.close()
f2.close()

print("\n--- Source File Content ---")
f1 = open(src, "r")
print(f1.read())
f1.close()

print("\n--- Destination File Content ---")
f2 = open(dest, "r")
print(f2.read())
f2.close()