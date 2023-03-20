import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ball = list(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    ball[a-1], ball[b-1] = ball[b-1], ball[a-1]
print(*ball)