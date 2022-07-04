class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


pos = Position('Игорь', 'Кечин', 'Data Scientist', {'wage': 20000, 'bonus': 5000})
print(pos.position)
pos.get_full_name()
pos.get_total_income()
