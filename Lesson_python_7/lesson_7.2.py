from abc import ABC, abstractmethod


class Clothes(ABC):
    exp_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.exp_count += self.expence

    def __str__(self):
        return f'Пальто: размер {self.size}, расход ткани {self.expence}, '\
                f'Общий расход ткани {Coat.exp_count:.02f}'

    @property
    def expence(self):
        exp = self.size/6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.exp_count += self.expence

    def __str__(self):
        return f'Костюм: рост {self.height}, расход ткани {self.expence}, '\
                f'Общий расход ткани {Costume.exp_count:.02f}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.02f}')


clothe1 = Coat(45)
print(clothe1)
clothe2 = Costume(181)
print(clothe2)
clothe3 = Costume(176)
print(clothe3)
clothe4 = Coat(50)
print(clothe4)