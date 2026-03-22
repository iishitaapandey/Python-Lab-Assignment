import numpy as np

print("Enter elements of 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

result = np.dot(A, B)

print("\nProduct Matrix:")
print(result)