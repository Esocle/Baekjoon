n, m = map(int, input().split())
ball = list(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    ball[a-1:b] = ball[a-1:b][::-1]
print(*ball)