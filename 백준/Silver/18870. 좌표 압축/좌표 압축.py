import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = sorted(set(arr))
res = {s[i]:i for i in range(len(s))}
for i in arr:
    print(res[i], end=' ')