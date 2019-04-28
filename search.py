#!/bin/python
# n iterations of the loop, O(n)
def search(list, key):
    for i in range(0, len(list)):
        if list[i] == key:
            return i
    return -1


print(search([1,2,3,4], 4) == 3)
print(search([1,2,3,4], 7) == -1)
print(search([1,2,3,4], 1) == 0)


# O (n log n)
def binary_search(l, key):
    l.sort()
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start+end)//2
        if l[mid] == key:
            return mid
        if key > l[mid]:
            start = mid + 1
        else: end = mid - 1
    return -1

print(binary_search([1,2,3,4], 4) == 3)
print(binary_search([1,2,3,4], 7) == -1)
print(binary_search([1,2,3,4], 1) == 0)
