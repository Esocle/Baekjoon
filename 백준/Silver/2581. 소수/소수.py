a = int(input())
b = int(input())
prime = []
for e in range(a, b+1):
    if e == 1:
        continue
    for i in range(2, e):
        if e % i == 0:
            break
    else:
        prime.append(e)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))