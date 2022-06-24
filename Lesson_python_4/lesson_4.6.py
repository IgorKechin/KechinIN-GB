from itertools import count
from itertools import cycle

for i in count(3, 1):
    print(i)
    if i == 10:
        break

s = 0
for i in cycle([1, 2, 3]):
    print(i)
    s += 1
    if s == 10:
        break

