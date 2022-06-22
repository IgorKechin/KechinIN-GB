def my_func(a,b,c):
    a = [a,b,c]
    a.remove(min(a))
    return a[0]+a[1]
print(my_func(a=3,b=2,c=1))