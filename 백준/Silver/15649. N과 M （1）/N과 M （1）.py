from itertools import permutations
n, m = map(int, input().split())
l = list(range(1, n+1))

for e in permutations(l, m):
    print(*e)