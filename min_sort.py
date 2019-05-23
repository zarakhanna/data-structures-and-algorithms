from random import sample
from time import time

l1 = sample(range(10**6), 10**4)
l2 = l1.copy()

def min_sort_lousy(l):
    for i in range(len(l)-1):
        smallest_num = 100000000000000
        smallest_pos = None
        for j in range(i, len(l)):
            if l[j] < smallest_num:
                smallest_num = l[j]
                smallest_pos = j
        l.pop(smallest_pos)
        l.insert(i, smallest_num)
    return l

def min_sort_good(l):
    for i in range(len(l)-1):
        smallest_num = 100000000000000
        smallest_pos = None
        for j in range(i, len(l)):
            if l[j] < smallest_num:
                smallest_num = l[j]
                smallest_pos = j
        l[i], l[smallest_pos] = l[smallest_pos], l[i]
    return l

N = 1

start = time()
for i in range(N):
    min_sort_lousy(l1)
end = time()
print("lousy", round(end - start, 3))

start = time()
for i in range(N):
    min_sort_good(l2)
end = time()
print("good", round(end - start, 3))
