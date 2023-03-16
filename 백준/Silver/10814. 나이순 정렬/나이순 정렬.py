import sys
input = sys.stdin.readline
n = int(input())
people = list(list(input().split()) for _ in range(n))
people.sort(key=lambda x : int(x[0]))
for e in people:
    print(*e)