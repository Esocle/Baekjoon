n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
money.sort(reverse=True)
cnt = 0
for m in money:
    if m <= k:
        tmp = k // m
        cnt += tmp
        k -= m * tmp
print(cnt)