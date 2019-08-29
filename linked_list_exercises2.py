from my_linked_lists import SingleNode, SinglyLinkedList, CircularLinkedList

def is_circular(linked_list):
    '''
    Returns True if linked_list is circular otherwise False
    '''
    c = linked_list.head
    while True:
        if c.nextnode == None:
            return False
        elif c.nextnode == linked_list.head:
            return True
        else:
            c = c.nextnode
    

def contains_loop(linked_list):
    '''
    Returns True if linked_list contains a loop within the links,
    otherwise False
    '''
    c = linked_list.head
    l = []
    while c != None:
        if c in l:
            return True
        else:
            l.append(c)
            c = c.nextnode
            continue
    return False

def print_case(s):
    l = len(s) + 4
    print('', '#'*l, '# ' + s + ' #', '#'*l, '', sep='\n')

print_case('Check not circular')
ll = SinglyLinkedList()
for i in range(10):
    ll.append(i)
print(is_circular(ll) == False)

print_case('Check circular')
ll = CircularLinkedList()
for i in range(10):
    ll.append(i)
print(is_circular(ll) == True)

print_case('Check does not contain loop')
ll = SinglyLinkedList()
for i in range(5):
    ll.append(i)
print(contains_loop(ll) == False)

print_case('Check contains loop')
ll = CircularLinkedList()
for i in range(10):
    ll.append(i)
print(is_circular(ll) == True)

from random import random
ll = SinglyLinkedList()
for i in range(10):
    ll.append(i)
curr_node = other_node = head_node = ll.get_head()
while isinstance(curr_node.nextnode, SingleNode):
    curr_node = curr_node.nextnode
    if random() < 0.3:
        other_node = curr_node
curr_node.nextnode = other_node
print(contains_loop(ll) == True)