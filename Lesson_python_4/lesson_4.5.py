from functools import reduce
def my_func (prev_val, val):
    return prev_val*val
print(reduce(my_func,[i for i in range(100,1001) if i % 2 == 0]))