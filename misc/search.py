#!/bin/python
# n iterations of the loop, O(n)
import sys
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

# MIN
def min(l):
     psn =  sys.maxint
     for i in l:
         if i < psn:
             psn = i
     return psn

print(min([3,2,6,5,1,4]) == 1)
print(min([3,2,6,-5,1,4]) == -5)
print(min([4]) == 4)

def max(l):
     psn =  -sys.maxint - 1
     for i in l:
         if i > psn:
             psn = i
     return psn

print(max([3,2,6,5,1,4]) == 6)
print(max([3,8,6,-5,1,4]) == 8)
print(max([4]) == 4)
