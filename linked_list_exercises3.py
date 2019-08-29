from my_linked_lists import SinglyLinkedList, DoublyLinkedList

def get_len(ll):
    c = ll.head
    s = 0
    while c != None:
        s += 1
        c = c.nextnode
    return s

def is_palindrome(singly_linked_list):
    '''Returns True if the singly_linked_list is a palindrone, False otherwise'''
    l = []
    c = singly_linked_list.head
    while c != None:
        l.append(c)
        c = c.nextnode
    return [i.val for i in list(reversed(l))] == [i.val for i in l]

def sort(doubly_linked_list):
    '''
    Takes in a doubly_linked_list,
    and returns a sorted DoublyLinkedList object
    '''
    # implementing selection in progress
    d = DoublyLinkedList()
    while get_len(doubly_linked_list) != 0:
        c = doubly_linked_list.head
        s = c
        while c != None:
            if c.val < s.val:
                s = c
            c = c.nextnode
        d.append(s.val)
        if s.prevnode != None:
            s.prevnode.nextnode = s.nextnode
        else:
            doubly_linked_list.head = s.nextnode
        if s.nextnode != None:
            s.nextnode.prevnode = s.prevnode
    return d

    # go through list
    # find smallest
    # pop
    # add 2 d
    # repeat till length is 0
    # return d


def print_case(s):
    l = len(s) + 4
    print('', '#'*l, '# ' + s + ' #', '#'*l, '', sep='\n')

print_case('Check get_len function')
ll = DoublyLinkedList()
print(get_len(ll))
for i in range(10):
    ll.append(i)
print(get_len(ll))

print_case("Check is_palindrome function")
sll = SinglyLinkedList()
for i in range(1,6):
    sll.append(i)
print(is_palindrome(sll) == False)
for i in range(5,0,-1):
    sll.append(i)
print(is_palindrome(sll) == True)

print_case('Check already sorted')
ll = DoublyLinkedList()
for i in range(10):
    ll.append(i)
print(sort(ll))

print_case('Check reversed list')
ll = DoublyLinkedList()
for i in range(9,-1,-1):
    ll.append(i)
print(sort(ll))

print_case('Check shuffled list')
from random import sample
ll = DoublyLinkedList()
for i in sample(range(10), 10):
    ll.append(i)
print(sort(ll))

