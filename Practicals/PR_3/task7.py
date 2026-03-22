# input using while loop
while True:
    a = int(input("Enter start number: "))
    b = int(input("Enter end number: "))
    
    if a < b:
        break
    else:
        print("Start should be less than end. Try again.")

print("\nPrime numbers:")

for num in range(a, b+1):
    if num > 1:
        is_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")