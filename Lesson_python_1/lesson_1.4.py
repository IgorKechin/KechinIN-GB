n = int(input('Введите целое положительное число: '))
max_number_list = []
while n > 0:
    max_number_list.append(n % 10)
    n = n//10
print(max(max_number_list))

