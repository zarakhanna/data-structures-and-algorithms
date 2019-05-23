from random import sample

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
    def __str__(self):
        return " ".join(map(str, self.l))

n = int(input("How many numbers would you like to play with? "))

s = Stack()
q = Queue()

for i in sample(range(1, 10*n+1), n):
    s.push(i)

# 2 actions:
# take off stack and queue up, OR
# leave the queue and place onto the stack.

# Take in user input and execute action.

while not s.is_sorted() or len(s.l) != n:
    user = input(f"""
Righty, folks.
If you type A,
    I'll take one item of the stack and queue it up,
or type B,
    I'll take an item off the queue and stack it.

Stack: {s} <-- Top of stack
Queue: {q} <-- Back of queue

Type here: """).upper()

    if user == "A":
        q.enqueue(s.pop())
    elif user == "B":
        s.push(q.dequeue())

print(f"""
Stack: {s} <-- Top of stack
Queue: {q} <-- Back of queue

SOOORRRRRTTTTEEEEEDDDDD!!!!!!!""")

# 1. Bring all the numbers to the queue

# 2. Find the biggest (unfrozen) number
# 3. Move numbers into the stack until biggest number is at front of queue
# 4. Queue up all (unfrozen) numbers from the stack to the queue.
# 5. Move biggest number over to the stack and then freeze it.

# 6. repeat from 2
