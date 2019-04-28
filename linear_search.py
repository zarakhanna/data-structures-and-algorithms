#!/bin/python
def search(list, key):
    for i in range(0, len(list)):
        if list[i] == key:
            return i
    return -1


print(search([1,2,3,4], 4) == 3)
print(search([1,2,3,4], 7) == -1)
print(search([1,2,3,4], 1) == 0)
