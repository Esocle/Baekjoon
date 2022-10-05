s = input()
temp = 'abcdefghijklmnopqrstuvwxyz'
for e in temp:
    if e in s:
        print(s.index(e), end = ' ')
    else:
        print(-1, end = ' ')