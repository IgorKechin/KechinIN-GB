def my_func1(x, y):
    return x**y
def my_func2(x, y):
    a = 1 / x
    for i in range(2, abs(y)+1):
        a *= 1/x
    return a


print (my_func1(8, -3))
print (my_func2(8, -3))