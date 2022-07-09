class MyOwnError(Exception):
    pass

in_data1 = input('Введите делимое: ')
in_data2 = input('Введите делитель: ')

try:
    in_data1 = int(in_data1)
    in_data2 = int(in_data2)
    if in_data2 == 0:
        raise MyOwnError('Делитель равен нулю!')

except MyOwnError as err:
    print(err)

else:
    print(in_data1 / in_data2)

