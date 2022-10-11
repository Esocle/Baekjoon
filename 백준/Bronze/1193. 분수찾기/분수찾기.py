n = int(input())
i = 1
while n > i:
    n -= i
    i += 1

if i%2 == 1:
    print(f"{i+1-n}/{n}")
else:
    print(f"{n}/{i+1-n}")