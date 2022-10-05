n = int(input())
for _ in range(n):
    iter, s = input().split(' ')
    iter = int(iter)
    answer = ''
    for e in s:
        answer += e*iter
    print(answer)