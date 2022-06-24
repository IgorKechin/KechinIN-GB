a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

b = [i for n, i in enumerate(a) if a[n] > a[n-1] and n != 0]
print(b)