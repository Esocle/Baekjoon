import sys
n = int(input())
number = [int(sys.stdin.readline()) for _ in range(n)]
number.sort()
for e in number:
    print(e)