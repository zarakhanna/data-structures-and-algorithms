from time import sleep
from random import shuffle, randint, choice

yays = ["Good!!", "Well done!!", "Excellent memory!", "Top prize for you!", "Guess is correct!", "Amazing!", "Epic work!!", "You've got a solid memory!", "Congratulations!"]
nays = ["Uh uh!!"]

delay = 10

items = "chicken eggs milk apple coconut yoghurt mango cherry fish ice_cream cake cheese".split()
shuffle(items)

class Stack:
    def __init__(self):
        self.l = []
    def pop(self):
        return self.l.pop()
    def push(self, item):
        self.l.append(item)
    def length(self):
        return len(self.l)

fridge = Stack()
num_of_items = int(input("How many items should we put into the fridge? "))
num_of_items = min(num_of_items, len(items))

for i in range(num_of_items):
    item = items[i]
    print(f"Placing {item} into the fridge...")
    fridge.push(item)
    sleep(1)

print("Remember the sequence!")
print(f"You have {delay} seconds...")
sleep(delay)
print("\n"*100)
slipups = 0
for i in range(fridge.length()):
    u = input("What are we taking out now? ").lower()
    item = fridge.pop()
    if u == item:
        print(f"{choice(yays)} Next!\n")
    else:
        print(f"{choice(nays)} It was actually {item}! Next!\n")
        slipups += 1

print(f"Cool! Your fridge is empty! You slipped up {slipups} times! Enjoy your fooood!")
