num = int(input())
total = 1
i = 0
while True:
    total += 6 * i
    if num <= total:
        break
    else:
        i += 1
print(i+1)