def int_func(w):
    return w.title()
words = input('Введите слова через пробел маленькими латинскими буквами: ').split()
print(' '.join(int_func(i) for i in words))