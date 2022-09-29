cube = list(map(int, input().split(" ")))
price = 0
temp = len(set(cube))
if temp == 1:
    price = 10000 + cube[0] * 1000
elif temp == 3:
    cube.sort()
    price = cube[2] * 100
else:
    if cube.count(cube[0]) == 2:
        price = 1000 + cube[0] * 100 
    else:
        price = 1000 + cube[1] * 100
print(price)