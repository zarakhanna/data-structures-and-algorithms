from linked_list_single import SinglyLinkedList, Node

class MyList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    def append(self,n):
        self.add_node(n)
    def pop(self):
        t = self.get_tail()
        self.remove_node()
        return t
    def length(self):
        return self.get_length()
    def insert(self, node, n):
         return self.insert_node(node,n)

n0 = Node("A")
n1 = Node("B")
n2 = Node("C")
n3 = Node("D")
l = MyList()
for n in [n0, n1, n2, n3]:
    l.append(n)
print(l.pop() is n3) # True
print(l.length() == 3) # True
l.insert(n3, 1)
print(l.pop() is n2) # True
print(l.pop() is n1) # True
print(l.pop() is n3) # True
print(l.pop() is n0) # True
print(l.length() == 0) # True
