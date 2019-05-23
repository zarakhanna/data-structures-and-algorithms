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

n = int(input("How many numbers would you like to play with? "))

s = Stack()
numbers = sample(range(1, 10*n+1), n)
holding = [numbers.pop()]
for i in sorted(numbers, reverse=True):
    s.push(i)

# 2 actions:
# pop stack OR push back numbers that are in your holding list

# Take in user input and execute action.

while not s.is_sorted() or s.length() != n:
    user = input(f"""
Righty, folks.
If you type A,
    I'll pop the stack
or type a number on the holding list,
    I'll push that number onto the stack.

Holding list: {holding}

Type here: """).upper()

    if user == "A":
        if len(numbers) == 1:
            print("STOP POP ONCE MORE ONLY11! THERE ARE NO NUMBERS LEFT!!")
        holding.append(s.pop())
    elif user.isnumeric() and int(user) in holding:
        holding.remove(int(user))
        s.push(int(user))
    else:
        print(f"I don't have the number {user}!!! ")

print(f"""
Stack: {s} <-- Top of stack

SOOORRRRRTTTTEEEEEDDDDD!!!!!!!""")

# 1. Bring all the numbers to the queue

# 2. Find the biggest (unfrozen) number
# 3. Move numbers into the stack until biggest number is at front of queue
# 4. Queue up all (unfrozen) numbers from the stack to the queue.
# 5. Move biggest number over to the stack and then freeze it.

# 6. repeat from 2
