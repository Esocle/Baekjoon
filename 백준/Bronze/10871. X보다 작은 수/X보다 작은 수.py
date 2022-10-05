n, x = map(int, input().split(" "))
temp = list(map(int, input().split(" ")))
for e in temp:
    if e < x: print(e, end=" ")