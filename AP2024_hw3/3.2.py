import numpy as np

class Arithmetics:
    def __init__(self, value):
        self._value = np.array(value)

    def __str__(self):
        return str(self._value)

    def __add__(self, other):
        return Arithmetics(self._value + other._value)

    def __sub__(self, other):
        return Arithmetics(self._value - other._value)

    def __mul__(self, other):
        return Arithmetics(self._value * other._value)

    def __truediv__(self, other):
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.true_divide(self._value, other._value)
            result[np.isinf(result)] = 0
            result = np.nan_to_num(result)
        return Arithmetics(result)

    def save_to_file(self, filename):
        np.savetxt(filename, self._value, fmt='%d')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = np.array(new_value)

np.random.seed(0)
matrix1 = Arithmetics(np.random.randint(0, 10, (10, 10)))
matrix2 = Arithmetics(np.random.randint(0, 10, (10, 10)))

add = matrix1 + matrix2
sub = matrix1 - matrix2
mul = matrix1 * matrix2
div = matrix1 / matrix2

print("+:\n", add)
print("-:\n", sub)
print("*:\n", mul)
print("/:\n", div)

add.save_to_file("add.txt")
sub.save_to_file("sub.txt")
mul.save_to_file("mul.txt")
div.save_to_file("div.txt")