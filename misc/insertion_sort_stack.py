class Stack:
    def __init__(self):
        self.l = [] #top of stack is right of list
    def pop(self):
        return self.l.pop()
    def push(self, item):
        self.l.append(item)
    def peek(self):
        return self.l[-1]
    def length(self):
        return len(self.l)
    def is_sorted(self):
        return self.l == sorted(self.l, reverse=True)
    def __str__(self):
        return " ".join(map(str, self.l))

def sorter(l,n):
    popl = []
    for i in l:
        if i>n:
            i.pop()
            popl.append(i)
        else:
            pass

# LEARN AN INSERTION SORT ALGORITHM

def insert_num(sorted_stack, num):
    """
    takes in a sorted stack, and integer num,
    inserts it into the (sorted) stack,
    returns the stack in sorted order
    note: only use pop, push, and length methods.
          do not use any built in sort functions
    """
    popl = []
    # stack is sorted from biggest number at the bottom
    #       to smallest number at the top
    # Need to put in a number, in the correct position in the stack.
    # I should keep on peeking/popping the stack until I get... (UNTIL is related to WHILE)
    #   a number that is bigger than our current number
    #   then my number to insert,
    #   then every other number back onto the stack.
    while sorted_stack.length() > 0 and sorted_stack.peek() < num:
        popl.append(sorted_stack.pop())
    sorted_stack.push(num)
    for i in popl[::-1]:
        sorted_stack.push(i)
    return sorted_stack

def insert_sort(list_of_numbers):
    """Takes in an unsorted list of numbers, returns a sorted stack"""
    # Step 1: start with empty stack
    s = Stack()
    for n in list_of_numbers:
        s = insert_num(s,n)
    return s


from random import sample

l1 = sample(range(1000), 5)
print("\n=== TEST CASE 1 ===")
print(*l1)
print(insert_sort(l1))

l2 = sample(range(1000), 10)
print("\n=== TEST CASE 2 ===")
print(*l2)
print(insert_sort(l2))
# test_stack = Stack()
# for n in [10,9,8,7,6,4,3,2,1]:
#     test_stack.push(n)
# print("\n=== TEST CASE 1 ===")
# print(test_stack)
# print(insert_num(test_stack, 5)) # 10 9 8 7 6 5 4 3 1
# test_stack = Stack()
# for n in [10,1]:
#     test_stack.push(n)
# print("\n=== TEST CASE 2 ===")
# print(test_stack)
# print(insert_num(test_stack, 5)) # 10 5 1
#
# test_stack = Stack()
# for n in [10,9,8]:
#     test_stack.push(n)
# print("\n=== TEST CASE 3 ===")
# print(test_stack)
# print(insert_num(test_stack, 5)) # 10 9 8 5
#
# test_stack = Stack()
# for n in [3,2,1]:
#     test_stack.push(n)
# print("\n=== TEST CASE 4 ===")
# print(test_stack)
# print(insert_num(test_stack, 5)) # 5 3 2 1
#
# test_stack = Stack()
# print("\n=== TEST CASE 5 ===")
# print(test_stack)
# print(insert_num(test_stack, 5)) # 5
