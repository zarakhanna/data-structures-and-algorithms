from random import sample
from time import sleep

class Stack:
    def __init__(self):
        self.l = [] #top of stack is right of list
    def pop(self):
        return self.l.pop()
    def push(self, item):
        self.l.append(item)
    def length(self):
        return len(self.l)
    def is_sorted(self):
        return self.l == sorted(self.l, reverse=True)
    def __str__(self):
        return " ".join(map(str, self.l))
class Queue:
    def __init__(self):
        self.l = [] #front of queue is left of list
    def dequeue(self):
        return self.l.pop(0)
    def enqueue(self, item):
        self.l.append(item)
    def length(self):
        return len(self.l)
    def get_biggest(self):
        return max(self.l)
    def peek(self):
        return self.l[0]
    def __str__(self):
        return " ".join(map(str, self.l))

n = int(input("How many numbers would you like to play with? "))
fnums = 0

s = Stack()
q = Queue()

def display_string(s, q):
    print(f"""Stack: {s} <-- Top of stack\nQueue: {q} <-- Back of queue\n\n""")
    sleep(0.5)

for i in sample(range(1, 10*n+1), n):
    s.push(i)

display_string(s, q)
# 1. Bring all the numbers to the queue
for i in range(s.length()):
    q.enqueue(s.pop())
    display_string(s, q)

# 6. repeat from 2
while not s.is_sorted() or s.length() < n:
    # 2. Find the biggest (unfrozen) number
    big = q.get_biggest()
    # 3. Move numbers into the stack until biggest number is at front of queue
    while q.peek() != big:
        s.push(q.dequeue())
        display_string(s, q)
    # 4. Queue up all (unfrozen) numbers from the stack to the queue.
    for i in range(s.length() - fnums):
        q.enqueue(s.pop())
        display_string(s, q)
    # 5. Move biggest number over to the stack and then freeze it.
    s.push(q.dequeue())
    display_string(s, q)
    fnums += 1
