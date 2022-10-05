import sys

n = int(sys.stdin.readline())

for i in range(n):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1+num2)