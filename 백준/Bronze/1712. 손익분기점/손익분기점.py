year, make, sale = map(int, input().split(' '))

if make >= sale:
    print(-1)
else:
    print(year//(sale-make)+1)