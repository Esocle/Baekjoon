A, B, V = map(int, input().split(" "))
days = (V-B) / (A-B)
if days != int(days):
    days += 1
print(int(days))