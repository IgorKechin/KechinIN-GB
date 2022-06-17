a = input('Введите список: ').split(',')
print(a)
for i in range(0, len(a), 2):
    if i + 1 <= len(a)-1:
        a[i], a[i + 1] = a[i + 1], a[i]
    else:
        break
print(a)
