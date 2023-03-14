import sys
from collections import deque

n, m = map(int, input().split())
b = list(range(1, n+1))
for _ in range(m):
    i, j, k = map(int, input().split())
    b[i-1:j] = b[k-1:j] + b[i-1:k-1]
print(*b)