t = int(input())
for _ in range(t):
    n, m = map(int, input().split(" "))
    a = m
    b = n

    for i in range(1, n):
        a *= m - i 
        b *= n - i 

    print(a // b)