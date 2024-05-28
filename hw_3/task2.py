import numpy as np


class FileOperations:
    def save(self, filepath):
        with open(filepath, "w") as handle:
            handle.write(str(self))


class MatrixOperation(np.lib.mixins.NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, Matrix):
                return NotImplemented

        inputs = tuple(x._matrix if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._matrix if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
    
class Matrix(MatrixOperation, FileOperations):
    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        return str(self._matrix)
    
    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix