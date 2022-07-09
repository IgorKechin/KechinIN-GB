class MyOwnError(Exception):
    pass


ls = []
while True:
    a = input('Введите число или Stop: ')
    if a == 'Stop':
        print(ls)
        break
    try:
        if a.isdigit():
            a = int(a)
            ls.append(a)
        else:
            raise MyOwnError('Введено не число!')
    except MyOwnError as err:
        print(err)
