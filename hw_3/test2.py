import numpy as np

from task2 import Matrix


np.random.seed(0)


a = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
b = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

a_plus_b = a + b
a_minus_b = a - b
a_mul_b = a * b
a_matmul_b = a @ b

a_plus_b.save("artifacts/32/matrix+.txt")
a_minus_b.save("artifacts/32/matrix-.txt")
a_mul_b.save("artifacts/32/matrix*.txt")
a_matmul_b.save("artifacts/32/matrix@.txt")

print(f"Matrix a is: {a}")
print("Set a is [[1, 2], [3, 4]]")
a.matrix = [[1, 2], [3, 4]]
print(f"Matrix a is: {a}")