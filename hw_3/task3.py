class HashMatrix:
    def __hash__(self) -> int:
        """Остаток от деления суммы диагональных элементов матрицы на 13

        Returns:
            int: Hash
        """
        length = min(self._shape[0], self._shape[1])
        summ = 0
        for i in range(length):
            summ += self._matrix[i][i]

        return summ % 13


class Matrix(HashMatrix):
    cache = {}

    def __init__(self, matrix) -> None:
        self._matrix = matrix
        self._shape = (len(self._matrix), len(self._matrix[0]))

    def __str__(self):
        return str(self._matrix)

    def __repr__(self):
        return str(self._matrix)

    def __add__(self, second):
        if self._shape != second._shape:
            raise ValueError(
                f"Matrix should the same shape, you put {self._shape} and {second._shape}")

        result = Matrix([[self._matrix[i][j] + second._matrix[i][j]
                        for j in range(self._shape[1])] for i in range(self._shape[0])])
        return result

    def __mul__(self, second):
        if self._shape != second._shape:
            raise ValueError(
                f"Matrix should the same shape, you put {self._shape} and {second._shape}")

        result = Matrix([[self._matrix[i][j] * second._matrix[i][j]
                        for j in range(self._shape[1])] for i in range(self._shape[0])])
        return result

    def __matmul__(self, second):
        if self._shape[1] != second._shape[0]:
            raise ValueError(
                f"Num columns in first matrix should equal num rows in second, you put {self._shape} and {second._shape}")

        key_cache = (hash(self), hash(second))

        if key_cache in Matrix.cache:
            result = Matrix.cache[key_cache]
        else:
            result = Matrix([[sum(self._matrix[i][k] * second._matrix[k][j] for k in range(second._shape[0]))
                              for j in range(second._shape[1])] for i in range(self._shape[0])])
        return result