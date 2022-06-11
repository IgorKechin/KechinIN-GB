a = int(input('Введите значение первого дня: '))
b = int(input('Введите значение порога: '))
i = 1
while a < b:
    i+=1
    a*=1.1
print(i)
