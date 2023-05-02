arr = []
for _ in range(9):
    temp = list(map(int, input().split()))
    arr.append(temp)
index = []
max = -999999
for i in range(9):
    for j in range(9):
        if(arr[i][j] > max): 
            max = arr[i][j]
            index = [i+1, j+1]
print(max)
print(*index)