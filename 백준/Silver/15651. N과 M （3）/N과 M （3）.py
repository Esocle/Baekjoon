from itertools import product
n, m = map(int, input().split())
l = list(range(1, n+1))

for e in product(l, repeat=m):
    print(*e)