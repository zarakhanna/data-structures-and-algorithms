class Node:
    def __init__(self, val):
        self.val = val
        self.prevnode = None
        self.nextnode = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def get_node(self,i):
        if i < 0:
            return None
        n = self.head
        for i in range(i):
            n = n.nextnode
        return n
    def get_length(self):
        l = 0
        if self.head == None:
            return l
        curr_node = self.head
        while curr_node.nextnode != None:
            l+=1
            curr_node = curr_node.nextnode
        l+=1
        return l
    def add_node(self,n):
        if self.tail == None:
            self.head = self.tail = n
            return
        self.tail.nextnode = n
        n.prevnode = self.tail
        self.tail = n
    def insert_node(self,n, p):
        i = self.get_node(p)
        if i == self.head:
            n.nextnode = i
            i.prevnode = n
            self.head = n
        elif i == self.tail:
            n.nextnode = i
            i.prevnode.nextnode = n
            n.prevnode = i.prevnode
            i.prevnode = n
        elif p >= self.get_length():
            self.tail.nextnode = n
            n.prevnode = self.tail
            self.tail = n
        elif i == None:
            self.head = self.tail = n
        else:
            i.prevnode.nextnode = n
            n.prevnode = i.prevnode 
            n.nextnode = i
            i.prevnode = n
    def pop_node(self, i):
        n = self.get_node(i)
        if n == self.head == self.tail:
            self.head = self.tail = None
            n.nextnode = n.prevnode = None
        elif n == self.head:
            self.head = n.nextnode
            n.nextnode.prevnode = None
            n.nextnode = None
        elif n == self.tail:
            n.prevnode.nextnode = None
            self.tail = n.prevnode
            n.prevnode = None
        else:
            n.prevnode.nextnode = n.nextnode
            n.nextnode.prevnode = n.prevnode
    def reverse_list(self):
        cnode = self.head
        for i in range(self.get_length()):
            cnode.nextnode,cnode.prevnode = cnode.prevnode, cnode.nextnode
            cnode = cnode.prevnode
        self.head,self.tail = self.tail,self.head

#   - __init__() : defines self.head a the head and self.tail as the tail
#   - get_node(i) : returns the node at position i, None otherwise
#   - add_node(node) : adds node at the tail of the linked list
#   - insert_node(node, i) : inserts node at position i in the linked list
#   - pop_node(i) : removes the node at position i
#   - reverse_list() : reverses the list so that the head is now the tail
#                      and vice versa

# Example codeu
dll = DoublyLinkedList()
print(dll.head == None) # True
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
dll.add_node(n0)
print(dll.head == n0) # True
print(dll.head == dll.get_node(0)) # True
print(dll.get_node(-1) == None) # True
dll.add_node(n1)
print(dll.get_node(1) == n1) # True
dll.add_node(n3)
print(dll.get_node(3) == None) # True
dll.insert_node(n2, 2)
print(dll.get_node(2) == n2) # True
print(dll.get_node(3) == n3) # True
dll.pop_node(1)
print(dll.get_node(1) == n2) # True
print(dll.get_node(2) == n3) # True
dll.pop_node(0)
print(dll.head == dll.get_node(0) == n2) # True
dll.insert_node(n1, 0)
dll.insert_node(n0, 0)
dll.insert_node(n4, 4) 
print(dll.get_node(4) == n4) # True
dll.reverse_list()
print(dll.get_node(0) == n4) # True
print(dll.get_node(1) == n3) # True
print(dll.get_node(2) == n2) # True
print(dll.get_node(3) == n1) # True
print(dll.get_node(4) == n0) # True