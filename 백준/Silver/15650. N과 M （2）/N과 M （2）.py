from itertools import combinations
n, m = map(int, input().split())
l = list(range(1, n+1))

for e in combinations(l, m):
    print(*e)