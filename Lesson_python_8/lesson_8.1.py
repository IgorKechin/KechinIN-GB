class Date:
    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def str_to_num(cls, dt):
        day, month, year = list(map(lambda x: int(x), dt.split('-')))
        return day, month, year

    @staticmethod
    def verify(self):
        spl = self.str_to_num(self.dt)
        if spl[0] > 31:
            raise ValueError ('Номер дня больше 31!')
        elif spl[1] > 12:
            raise ValueError ('Номер месяца больше 12!')
        else:
            return 'Все в порядке!'


d_1 = Date('12-10-1987')
print(d_1.str_to_num('12-10-1987'))
print(d_1.verify(d_1))
