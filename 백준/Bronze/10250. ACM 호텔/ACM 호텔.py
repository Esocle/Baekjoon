tmp = int(input())
for _ in range(tmp):
    H, W, N = map(int, input().split(' '))
    if N%H == 0:
        print(f'{H}{N//H:02d}')
    else:
        print(f'{N%H}{N//H+1:02d}')