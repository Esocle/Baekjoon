year, make, sale = map(int, input().split(' '))

if make >= sale:
    print(-1)
else:
    print(int(year/(sale-make))+1)