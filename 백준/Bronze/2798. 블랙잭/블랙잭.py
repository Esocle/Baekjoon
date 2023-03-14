import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0

for e in combinations(card, 3):
    if sum(e) > res and sum(e) <= m:
        res = sum(e)
print(res)