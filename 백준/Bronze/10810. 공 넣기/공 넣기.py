import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ball = list(0 for _ in range(n))
for _ in range(m):
    a, b, c = map(int, input().split())
    ball[a-1:b] = [c for _ in range(a-1, b)]
print(*ball)