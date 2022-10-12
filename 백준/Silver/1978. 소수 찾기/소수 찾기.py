n = int(input())
nums = list(map(int, input().split(' ')))
for e in nums:
    if e == 1:
        n -= 1
    for i in range(2, e):
        if e%i == 0:
            n -= 1
            break
print(n)