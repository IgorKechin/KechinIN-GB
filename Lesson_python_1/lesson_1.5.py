val_1 = int(input('Введите значение выручки: '))
ex_1 = int(input('Введите значение издержек: '))
if val_1 > ex_1:
    print('Прибыль')
elif val_1 < ex_1:
    print('Убыток')
else:
    print('0')