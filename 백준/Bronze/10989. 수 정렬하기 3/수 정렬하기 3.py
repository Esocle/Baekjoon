import sys

counting = [0 for _ in range(10001)]
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    counting[num] += 1

for i in range(1, 10001):
    count = counting[i]
    for _ in range(count):
        print(i)