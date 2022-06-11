val_1 = int(input('Введите значение выручки: '))
ex_1 = int(input('Введите значение издержек: '))
if val_1 > ex_1:
    print('Прибыль')
    print('Рентабельность выручки - ', round((val_1 - ex_1)/ex_1, 4))
    staf = int(input('Введите число сотрудников: '))
    print('Прибыль на одного сотрудника - ', round((val_1 - ex_1)/staf, 4))
elif val_1 < ex_1:
    print('Убыток')
else:
    print('0')