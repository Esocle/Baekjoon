price = int(input())
iter = int(input())
for i in range(iter):
    a, b = map(int, input().split(" "))
    price -= a * b
print("Yes" if price == 0 else "No")