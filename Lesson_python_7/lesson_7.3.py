class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row_len):
        result = ['*' * row_len] * (self.nums // row_len)
        if self.nums % row_len:
            result.append('*' * (self.nums % row_len))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums < other.nums:
            raise ValueError('Ячеек в первой клетке меньше второй!')
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        return Cell(self.nums // other.nums)


cell1 = Cell(15)
cell2 = Cell(24)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell1.make_order(7))
