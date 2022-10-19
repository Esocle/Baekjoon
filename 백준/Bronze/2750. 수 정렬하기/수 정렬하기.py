n = int(input())
number = [int(input()) for _ in range(n)]

### 삽입 정렬
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if number[min_index] > number[j]:
            min_index = j
    number[i], number[min_index] = number[min_index], number[i]
    
for e in number:
    print(e)