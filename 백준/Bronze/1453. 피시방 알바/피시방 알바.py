n = int(input())
cnt = 0
temp = list(map(int, input().split()))
counts = []
for e in temp:
    if e not in counts:
        counts.append(e)
    else:
        cnt += 1
print(cnt)