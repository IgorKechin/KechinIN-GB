def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
print(func(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
