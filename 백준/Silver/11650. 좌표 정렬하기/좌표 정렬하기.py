import sys
input = sys.stdin.readline
n = int(input())
points = list(tuple(map(int, input().split())) for _ in range(n))
points.sort()
for e in points:
    print(*e)