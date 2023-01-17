n, m = map(int, input().split())
h1 = []
h2 = []
for i in range(n):
    temp = list(map(int, input().split()))
    h1.append(temp)
for i in range(n):
    temp = list(map(int, input().split()))
    h2.append(temp)
for i in range(n):
    for j in range(m):
        print(h1[i][j]+h2[i][j], end = ' ')
    print()