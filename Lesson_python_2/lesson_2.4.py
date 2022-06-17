a = input('Введите слова через пробел: ').split(' ')
for i,p in enumerate(a):
    print(i,p[:10])