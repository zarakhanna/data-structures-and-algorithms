class SingleNode:
    def __init__(self, val):
        self.nextnode = None
        self.val = val

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def append(self, val):
        node = SingleNode(val)
        if self.head == None:
            self.head = node
            return
        last = self.head             # set initial current node
        while last.nextnode != None: # loop to the end
            last = last.nextnode     # update current node
        last.nextnode = node         # set up link
    def pop(self):
        if self.head == None: raise Exception('list is empty')
        if self.head.nextnode == None:
            last = self.head
            self.head = None
            return last.val
        second_last = self.head                      # set initial current node
        while second_last.nextnode.nextnode != None: # loop to the second last
            second_last = second_last.nextnode       # update current node
        last = second_last.nextnode                  # grab reference to last node
        second_last.nextnode = None                  # break link to last
        return last.val                              # return the last node value
    def __str__(self):
        curr = self.head
        if curr == None:
            return 'empty'
        else:
            l = []
            while curr != None:
                l.append(curr.val)
                curr = curr.nextnode
            return ' -> '.join(map(str,l))

class DoubleNode(SingleNode):
    def __init__(self, val):
        self.prevnode = None
        super().__init__(val)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def append(self, val):
        node = DoubleNode(val)
        if self.head == None:
            self.head = node
            return
        last = self.head      # set initial current node
        while last.nextnode != None:    # loop i times
            last = last.nextnode # update current node
        last.nextnode = node      # set up double links
        node.prevnode = last       #
    def pop(self):
        if self.head == None: raise Exception('list is empty')
        if self.head.nextnode == None:
            last = self.head
            self.head = None
            return last.val
        last = self.head      # set initial current node
        while last.nextnode != None:    # loop i times
            last = last.nextnode # update current node
        second_last = last.prevnode
        second_last.nextnode = None
        last.prevnode = None
        return last.val
    def __str__(self):
        curr = self.head
        if curr == None:
            return 'empty'
        else:
            l = []
            while curr != None:
                l.append(curr.val)
                curr = curr.nextnode
            return ' <-> '.join(map(str,l))

# Create a class CircularLinkedList that inherits from SinglyLinkedList
# override method append(val) : ensure that inserted node links back to head.
# override method pop() : ensure that 'last' node is removed and the new 'last' links back to head.
# add new method rotate() : rotates the head forward 1 step.
# add new method rotate_n(n) : rotates the head forward n steps.
# override __str__() : add representation to loop back around
class CircularLinkedList(SinglyLinkedList):
    def append(self, val):
        node = SingleNode(val)
        if self.head == None:
            self.head = node
            node.nextnode = self.head
            return
        last = self.head                  # set initial current node
        while last.nextnode != self.head: # loop to the end
            last = last.nextnode          # update current node
        last.nextnode = node              # set up link
        node.nextnode = self.head
    def pop(self):
        if self.head == None: raise Exception('list is empty')
        if self.head.nextnode == self.head:
            last = self.head
            self.head = None    
            return last.val
        last = self.head      # set initial current node
        while last.nextnode != self.head:    # loop i times
            last = last.nextnode # update current node
        sl = self.head
        while sl.nextnode != last:    # loop i times
            sl = sl.nextnode
        sl.nextnode = self.head
        last.nextnode = None
        return last.val
    def rotate(self):
        if self.head == None: raise Exception('list is empty')
        self.head = self.head.nextnode
    def rotate_n(self,n):
        if self.head == None: raise Exception('list is empty')
        for i in range(n):
            self.rotate()
    def __str__(self):
        
        if self.head == None: return 'empty'
        curr = self.head
        l = [curr.val]
        while curr.nextnode != self.head:
            curr = curr.nextnode
            l.append(curr.val)
        return ' -> '.join(map(str,l)) + " -> HEAD"