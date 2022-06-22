def my_func():
    r = 0
    l = input('Введите числа через пробел или q для выхода: ').split()
    for i in l:
        if i == 'q':
            return r, True
        else:
            r += float(i)
    return r, False

res = 0
while True:
    a, b = my_func()
    res += a
    print(res)
    if b:
        break

