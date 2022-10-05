n = int(input())
l = [input() for e in range(n)]
for e in l:
    temp = 0
    total = 0
    for i in range(len(e)):
        if e[i] == 'O':
            temp += 1
            total += temp
        else:
            temp = 0
    print(total)