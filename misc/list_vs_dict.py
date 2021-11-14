from random import sample, randint
from time import time

numbers = sample(range(10**6), 10**4)

mylist = list(numbers)
myhash = set(numbers)

list_time = 0
hash_time = 0

for _ in range(1000):
    num = randint(0,10**6-1)
    # check if num exists
    start = time()
    num in mylist
    list_time += time()-start
    start = time()
    num in myhash
    hash_time += time()-start

print('list took', list_time)
print('hash took', hash_time)