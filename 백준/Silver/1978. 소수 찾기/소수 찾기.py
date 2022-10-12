n = int(input())
cnt = 0
nums = list(map(int, input().split(' ')))
def is_prime(e):
    if e == 1:
        return 0
    for i in range(2, e):
        if e%i == 0:
            return 0
    return 1
for e in nums:
    cnt += is_prime(e)
print(cnt)