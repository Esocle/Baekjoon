a, b = map(int, input().split())
num = a * b
temp = list(map(int, input().split()))
for e in temp:
    print(e-num, end = ' ')