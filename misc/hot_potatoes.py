from time import sleep

class Queue:
    def __init__(self):
        self.q = []
        # start of queue is left side of list
        # end of queue is right side of list
    def enqueue(self, item):
        self.q.append(item)
    def dequeue(self):
        return self.q.pop(0)
    def length(self):
        return len(self.q)

n = int(input("How many people are playing HOT POTATOES? "))

names = Queue()
for i in range(1, n+1):
    name = input(f"What is the name of Person {i}? ")
    names.enqueue(name)

_syllables = ["Hot", "Poe", "Tae", "Toe"]*3 + ["BURNT!!!"]
syllables = Queue()
for s in _syllables:
    syllables.enqueue(s)

while names.length() != 1:
    sleep(0.3)
    name = names.dequeue()
    syllable = syllables.dequeue()
    print(f"{name.rjust(10)} says {syllable}")
    if syllable == "BURNT!!!":
        print(f"{name}'s OUT!!'")
        syllables.enqueue(syllable)
        sleep(0.5)
    else:
        names.enqueue(name)
        syllables.enqueue(syllable)
print(f"{names.dequeue()} is the WIIINNNNEEEERRRRRRRRR!")
