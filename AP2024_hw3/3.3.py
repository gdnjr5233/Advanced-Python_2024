import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

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


class Hashable:
    def __hash__(self):
        return int(np.sum(self.data) + self.data.shape[0] * self.data.shape[1])


class HashableMatrix(Matrix, Hashable):
    def __init__(self, data):
        super().__init__(data)
    
    _cache = {}
    
    def __matmul__(self, other):
        hash_result = self.__hash__(), other.__hash__()
        if hash_result in self._cache:
            print("result found in cache!")
            return self._cache[hash_result]
        result = super().__matmul__(other)
        self._cache[hash_result] = result
        return result
    

def find_collision():
    hashes = {}
    np.random.seed(0)
    while True:
        new_matrix = HashableMatrix(np.random.randint(0, 10, (10, 10)))
        new_hash = hash(new_matrix)
        if new_hash in hashes:
            if not np.array_equal(new_matrix.data, hashes[new_hash].data):
                return new_matrix, hashes[new_hash]
        else:
            hashes[new_hash] = new_matrix


A, C = find_collision()
B = HashableMatrix(np.random.randint(0, 10, (10, 10)))
D = B

AB = A @ B
CD = C @ D

hash_AB = hash(AB)
hash_CD = hash(CD)

A.save_to_file("A.txt")
B.save_to_file("B.txt")
C.save_to_file("C.txt")
D.save_to_file("D.txt")
AB.save_to_file("AB.txt")
CD.save_to_file("CD.txt")

with open("hash.txt", "w") as f:
    f.write(f"Hash of AB: {hash_AB}\n")
    f.write(f"Hash of CD: {hash_CD}\n")