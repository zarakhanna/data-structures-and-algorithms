from my_linked_lists import DoublyLinkedList, SinglyLinkedList, CircularLinkedList

l = DoublyLinkedList()
# get_head: returns head node object
# append: returns nothing, but adds a node with val at the back
# pop: returns you the val of the last node, and removes it from list
print(l)

for i in range(7):
    l.append(i)

m = DoublyLinkedList()
for i in range(10,15):
    m.append(i)

# print(l)
# print(m)

# 1. Combine linked lists l and m, without creating a new linked list.
def get_tail(l):
    curr = l.get_head()
    while curr.nextnode != None:
        curr = curr.nextnode
    return curr

t = get_tail(l)
# print(t.val, "lookie here!")
t.nextnode = m.get_head()
m.get_head().prevnode = t

print(l)

def get_sum(l):
    curr = l.get_head()
    sumd = 0
    while curr != None:
        sumd += curr.val
        curr = curr.nextnode
    return sumd


# print("HEEEEEEEEEREEEEEEEEIE!")
# print(get_sum(l))
# print(get_sum(l) == (0+1+2+3+4+5+6+10+11+12+13+14))
# print(0+1+2+3+4+5+6+10+11+12+13+14, "HEREHERE")

from random import sample, seed
seed(0)
n = DoublyLinkedList()
for i in sample(range(100), 10):
    n.append(i)
print(n)

def get_max(l):
    curr = l.get_head()
    l = []
    while curr != None:
        l.append(curr.val)
        curr = curr.nextnode
    return max(l)
def get_min(l):
    curr = l.get_head()
    l = []
    while curr != None:
        l.append(curr.val)
        curr = curr.nextnode
    return min(l)

# print(get_max(n) == 97)
# print(get_min(n) == 5)

# print(get_max(n),"  max heerrroooooooooooooooo")
# print(get_min(n),"  min heerrriiiiiieeeeeeeeee")

# REVERSE m.

m = DoublyLinkedList()
for i in range(10,15):
    m.append(i)

def reverse(l):
    tail = get_tail(l)
    cnode = l.get_head()
    while cnode != None:
        cnode.nextnode, cnode.prevnode = cnode.prevnode, cnode.nextnode
        cnode = cnode.prevnode
    l.head = tail
    return l

# print("YAY!")
# print(m)
# print(reverse(m))
# print(m == reverse(reverse(m)))

s = SinglyLinkedList()
for i in range(1,12):
    s.append(i)
print(s)

'''
snake_case
SCREAMING_SNEK_CASE
camelCase
PascalCase
aNnOyInGcAsE
'''

def get_length(l):
    cnode = l.head
    le = 0
    while cnode != None:
        cnode = cnode.nextnode
        le += 1
    return le

def single_reverse(l):
    ll = SinglyLinkedList()
    length = get_length(l)
    for i in range(length):
        ll.append(l.pop())
    return ll


print("\nYoohoo!!\n")

print(single_reverse(s))


c = CircularLinkedList()
for i in range(15):
    c.append(i)
print(c)
for i in range(5):
    print(c.pop())
print(c)
c.rotate()
print(c)
c.rotate_n(9)
print(c)
