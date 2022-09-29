H, M = map(int, input().split(" "))
time = int(input())

if M + time >= 60:
    H += (M+time)//60
    M = (M+time)%60
    if H >= 24:
        H %= 24
else:
    M += time

print(H, M)