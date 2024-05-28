from task3 import Matrix
import numpy as np

cache = {}
pbar = 0
while True: # ищем а и с
    pbar += 1
    print(pbar)
    matrix = Matrix(np.random.randint(0, 10, (2, 2)).tolist())
    m_hash = hash(matrix)
    if (m_hash in cache) and matrix != cache[m_hash]:
        a = matrix
        c = cache[m_hash]
        break
    cache[m_hash] = matrix

while True: # ищем b и d
    b_d = Matrix(np.random.randint(0, 10, (2, 2)).tolist())
    if a @ b_d != c @ b_d:
        print(a, c, b_d)
        break

# финальная проверка
assert (hash(a) == hash(c)) and (a != c) and (a @ b_d != c @ b_d)

with open("artifacts/33/A.txt", "w") as handle:
    handle.write(repr(a))
with open("artifacts/33/B.txt", "w") as handle:
    handle.write(repr(b_d))
with open("artifacts/33/C.txt", "w") as handle:
    handle.write(repr(c))
with open("artifacts/33/D.txt", "w") as handle:
    handle.write(repr(b_d))

with open("artifacts/33/AB.txt", "w") as handle:
    handle.write(repr(a @ b_d))
with open("artifacts/33/CD.txt", "w") as handle:
    handle.write(repr(c @ b_d))
with open("artifacts/33/hash.txt", "w") as handle:
    handle.write("\n".join([str(hash(a @ b_d)), str(hash(c @ b_d))]))