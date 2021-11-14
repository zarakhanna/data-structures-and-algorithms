# keeps every single word typed
# except when you say "repeat", then print the first item
# if there is none left when you say "repeat", throw an error

l = []

while True:
    i = input("Type a word:    ")
    i = i.lower()
    if i == "repeat":
        print(l.pop(0)) 
    else:
        l.append(i)
