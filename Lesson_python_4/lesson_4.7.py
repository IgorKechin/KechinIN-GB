from functools import reduce
def my_func(prev_val, val):
    return prev_val * val

def fact(n):
    for i in range(1, n+1):
        yield reduce(my_func, [v for v in range(1, i+1)])

for el in fact(5):
    print(el)