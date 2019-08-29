class Node:
    def __init__(self, name):
       self.name = name
       self.nextnode = None
    def get_value(self):
       return self.name
    def set_next(self, Node):
        self.nextnode = Node
    def get_next(self):
       return self.nextnode
    def __str__(self):
        return f"(NodeObject: {self.name})"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def add_node(self, node):
        if self.head == None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            curr_node.set_next(node)
    def get_length(self):
        l = 0
        if self.head == None:
            return l
        curr_node = self.head
        while curr_node.get_next() != None:
            l+=1
            curr_node = curr_node.get_next()
        l+=1
        return l
    def get_nth_node(self, n):
        curr_node = self.head
        for i in range(n):
            if curr_node.get_next() == None:
                return None
            else:
                curr_node = curr_node.get_next()
        return curr_node
    def get_head(self):
        return self.get_nth_node(0)
    def get_tail(self):
        return self.get_nth_node(self.get_length()-1)
    def insert_node(self, node, n):
        # if n == 0:
        #     node.set_next(self.get_head(0))
        #     self.head = node
        #     return
        # max_length = self.get_length()
        # if n > max_length:
        #     n = max_length
        # left = self.get_nth_node(n-1)
        # right = left.get_next()
        # left.set_next(node)
        # node.set_next(right)
        curr_node = self.head
        prev = None
        if n == 0:
            self.head = node
            node.nextnode = curr_node
            return 
            
        for i in range(n):
            if curr_node.get_next() == None:
                curr_node.nextnode = node
                return
            else:
                prev = curr_node
                curr_node = curr_node.get_next()
                
        node.nextnode = curr_node
        if node != self.head and prev!=None:
            prev.nextnode = node
    def remove_node(self):
        if self.get_length() == 1:
            self.head = None
        if self.get_length() == 0:
            return
        bt = self.get_nth_node(self.get_length()-2)
        bt.nextnode = None


# n0 = Node("Alex")
# n1 = Node("Beth")

# print(n0.get_value()) # "Alex"
# print(n0.get_next()) # None
# print(n0.set_next(n1)) # None
# print(n0.get_next() is n1) # True
# print(n0.get_next().get_value()) # Beth

# print("end")

# n0 = Node("Alex")
# n1 = Node("Beth")
# n2 = Node("Carl")
# n3 = Node("Dion")

# ll = SinglyLinkedList()
# ll.add_node(n0)
# ll.add_node(n1)
# ll.add_node(n2)
# ll.add_node(n3)
# print(ll.get_head().get_value()) # Alex
# print(ll.get_length()) # 4
# print(ll.get_tail() is n3) # True
# print(ll.get_tail(), "<------------------ LOOK HERE")
# print(ll.get_nth_node(0) is n0)
# print(ll.get_nth_node(1) is n1)
# print(ll.get_nth_node(2) is n2)
# print(ll.get_nth_node(3) is ll.get_tail())

# print(ll.get_nth_node(0), "<------------------ LOOKee HEREee")
# print(ll.get_nth_node(1), "<------------------ LOOKee HEREee")
# print(ll.get_nth_node(2), "<------------------ LOOKee HEREee")
# print(ll.get_nth_node(3), "<------------------ LOOKee HEREee")

# print(ll.get_nth_node(4) is None)
# print(ll.get_nth_node(5) is None)
# print(ll.get_nth_node(9) is None, "<------------------ LOOK HERE")


# print("Inserting in the middle")
# n0 = Node("Alex")
# n1 = Node("Beth")
# n2 = Node("Carl")
# n3 = Node("Dion")

# ll2 = SinglyLinkedList()
# ll2.add_node(n3)
# ll2.add_node(n2)
# ll2.add_node(n1)
# print(ll2.get_head().get_value()) # Dion
# print(ll2.get_head().get_next().get_value()) # Carl
# print(ll2.get_head().get_next().get_next().get_value()) # Beth
# print(ll2.get_length()) # 3
# print(ll2.get_tail() is n1) # True

# print(ll2.get_nth_node(0) is n3) # True
# print(ll2.get_nth_node(1) is n2) # True
# print(ll2.get_nth_node(2) is n1) # True
# ll2.insert_node(n0, 3)
# print(ll2.get_nth_node(0) is n3) # True
# print(ll2.get_nth_node(1) is n2) # True
# print(ll2.get_nth_node(2) is n1) # True
# print(ll2.get_nth_node(3) is n0) # True

# print(ll2.get_nth_node(1),"     LAAAAAA") # True
# print(ll2.get_nth_node(2),"     LAAAAAA") # True



# print("Testing add front")
# n0 = Node("Alex")
# n1 = Node("Beth")

# ll = SinglyLinkedList()
# ll.add_node(n0)
# ll.insert_node(n1, 0)
# print(ll.get_head() is n1) # True
# print(ll.get_tail() is n0, ll.get_tail(), ll.get_length()) # True



# print("Testing add back")
# n0 = Node("Alex")
# n1 = Node("Beth")

# ll = SinglyLinkedList()
# ll.add_node(n0)
# ll.insert_node(n1, 1)
# print(ll.get_head() is n0) # True
# print(ll.get_tail() is n1) # True ????


# print("Testing add out of index")
# n0 = Node("Alex")
# n1 = Node("Beth")

# ll = SinglyLinkedList()
# ll.add_node(n0)
# ll.insert_node(n1, 99)
# print(ll.get_head() is n0) # True
# print(ll.get_tail() is n1) # True


# print("Testing remove tail")
# n0 = Node("Alex")
# n1 = Node("Beth")

# ll = SinglyLinkedList()
# ll.add_node(n0)
# ll.add_node(n1)
# print(ll.get_tail() is n1) # True 
# ll.remove_node()
# print(ll.get_tail() is n0) # True
# ll.remove_node()
# print(ll.get_tail()) # True