num = 1
while True:
    n = int(input())
    if n == 0:
        break
    names = [input() for _ in range(n)]
    tmp = []
    for _ in range(n*2 - 1):
        a, b = input().split()
        tmp.append(int(a))
    for i in range(1, n+1):
        c = tmp.count(i)
        if c == 1:
            print(num, names[i-1])
            num += 1
    names = []
    tmp = []