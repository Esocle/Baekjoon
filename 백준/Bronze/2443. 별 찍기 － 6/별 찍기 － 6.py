n = int(input())
for i in range(n, 0, -1):
    e = 2*i - 1
    print(' '*(n - i) + '*'*e)