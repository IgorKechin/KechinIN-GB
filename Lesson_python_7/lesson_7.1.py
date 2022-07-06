class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return '\n'.join(('\t'.join(str(num) for num in line)) for line in self.matr)

    def __add__(self, other):
        data = [[(int(self.matr[line][num]) + int(other.matr[line][num])) for num in
                 range(len(self.matr[line]))] for line in range(len(self.matr))]
        return Matrix(data)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[6, 5, 4], [3, 2, 1]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
