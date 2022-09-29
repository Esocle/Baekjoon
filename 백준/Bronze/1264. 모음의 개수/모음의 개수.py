temp = []
while True:
    e = input()
    if e == "#":
        break
    temp.append(e)
for s in temp:
    print(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') 
    + s.count('A') + s.count('E') + s.count('I') + s.count('O') + s.count('U'))