from itertools import combinations_with_replacement
n, m = map(int, input().split())
l = list(range(1, n+1))

for e in combinations_with_replacement(l, m):
    print(*e)