temp = int(input())
for _ in range(temp):
    l = list(map(int, input().split(' ')))
    avg = (sum(l[1:])) / l[0]
    cnt = 0
    for e in l[1:]:
        if e > avg:
            cnt +=1
    print(f'{cnt/l[0]*100:.3f}%')