import numpy as np

from task1 import Matrix


np.random.seed(0)


a = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
b = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

with open("artifacts/31/matrix+.txt", "w") as handle:
    handle.write(repr(a + b))

with open("artifacts/31/matrix*.txt", "w") as handle:
    handle.write(repr(a * b))

with open("artifacts/31/matrix@.txt", "w") as handle:
    handle.write(repr(a @ b))