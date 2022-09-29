H, M = map(int, input().split(" "))
if H == 0:
    if M > 44:
        print(H, M-45)
    else:
        print(23, 60+(M-45))
else:
    if M > 44:
        print(H, M-45)
    else:
        print(H-1, 60+(M-45))