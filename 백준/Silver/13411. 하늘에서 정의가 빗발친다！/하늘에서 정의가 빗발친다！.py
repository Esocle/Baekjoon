import sys
import math

distance = []
n = int(sys.stdin.readline())

for i in range(1, n+1):
    x, y, v = map(int, sys.stdin.readline().split())
    distance.append((i, v / math.sqrt(x**2 + y**2)))
distance.sort(key=lambda x:-x[1])
for i in range(n):
    print(distance[i][0])