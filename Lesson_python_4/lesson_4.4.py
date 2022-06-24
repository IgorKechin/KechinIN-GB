import numpy as np
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

uniq_list = set()
rep_list = set()

for i in a:
    if i in rep_list:
        continue
    if i in uniq_list:
        rep_list.add(i)
        uniq_list.discard(i)
        continue
    uniq_list.add(i)
print(uniq_list)

print([i for i in a if i in uniq_list])
