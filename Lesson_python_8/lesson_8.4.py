class StockOrgTeh:
    def __init__(self):
        self.stock = {}

    def arrival(self, goods, num):
        if type(num) == int:
            if goods in self.stock:
                self.stock[goods] = self.stock[goods] + num
            else:
                self.stock[goods] = num
        else:
            print('Количество должно быть числом!')

    def consum(self, goods, num):
        if type(num) == int:
            try:
                if self.stock[goods] > num:
                    self.stock[goods] = self.stock[goods] - num
                elif self.stock[goods] == num:
                    del self.stock[goods]
                else:
                    print('Не хватает товара на складе!')
            except (KeyError):
                print('Не хватает товара на складе!')
        else:
            print('Количество должно быть числом!')


class OrgTeh:
    def __init__(self, num_ser):
        self.num_ser = num_ser


class Printers(OrgTeh):
    def __init__(self, type_printer):
        self.type_printer = type_printer


class Scaner(OrgTeh):
    def __init__(self, type_scaner):
        self.type_scaner = type_scaner


class Xerox(OrgTeh):
    def __init__(self, type_xerox):
        self.type_xerox = type_xerox


st = StockOrgTeh()
st.arrival('scaner', 5)
print(st.stock)
st.consum('scaner', 2)
print(st.stock)
