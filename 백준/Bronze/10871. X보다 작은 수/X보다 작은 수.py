n, x = map(int, input().split(" "))
temp = [e for e in input().split(" ") if int(e) < x]
print(' '.join(temp))