import sys
from collections import deque

n = int(input())
q = deque(range(1, n+1))

while True:
    if len(q) == 1: break
    q.popleft()
    q.rotate(-1)
print(*q)