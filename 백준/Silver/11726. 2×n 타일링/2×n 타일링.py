n = int(input())
if n == 1:
    res = 1
elif n == 2:
    res = 2
elif n >= 3:
    temp = [0] * n
    temp[0] = 1
    temp[1] = 2
    
    for i in range(2, n):
        temp[i] = temp[i-1] + temp[i-2]
        
    res = temp[i] % 10007
print(res)