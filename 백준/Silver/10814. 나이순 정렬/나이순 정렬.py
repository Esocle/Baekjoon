import sys
input = sys.stdin.readline
n = int(input())
people = list(list(input().split()) for _ in range(n))
for e in people:
    e[0] = int(e[0])
people.sort(key=lambda x : x[0])
for e in people:
    print(*e)