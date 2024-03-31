import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrix dimensions must match to be added")
        return Matrix(self.data + other.data)
    
    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrix dimensions must match for element-wise multiplication")
        return Matrix(self.data * other.data)
    
    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrix dimensions are not compatible with matrix multiplication")
        return Matrix(np.matmul(self.data, other.data))
    
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

result_add = matrix1 + matrix2
result_mul = matrix1 * matrix2
result_matmul = matrix1 @ matrix2

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

result_add.save_to_file("matrix+.txt")
result_mul.save_to_file("matrix_asterisk.txt")
result_matmul.save_to_file("matrix@.txt")