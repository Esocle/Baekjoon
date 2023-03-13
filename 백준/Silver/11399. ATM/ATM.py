import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().strip().split()))
h.sort()
cnt = 0
for i in range(n):
    cnt += sum(h[:i+1])
print(cnt)