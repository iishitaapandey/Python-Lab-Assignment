import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

add = A + B
mul = np.dot(A, B)

print("\nAddition:\n", add)
print("\nMultiplication:\n", mul)