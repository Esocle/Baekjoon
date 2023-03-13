import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    k = int(input())
    if k == 0:
        stack.pop()
    else:
        stack.append(k)
print(sum(stack))