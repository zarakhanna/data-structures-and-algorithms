# keeps every single word typed, in a list
# except when you say "repeat", then pop the last item from the list
# if the list is empty when you say "repeat", throw an error

l = []

while True:
    i = input("Type a word:    ")
    i = i.lower()
    if i == "repeat":
        print(l.pop())
    else:
        l.append(i)
