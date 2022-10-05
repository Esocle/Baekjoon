temp = int(input())
for _ in range(temp):
    l = list(map(int, input().split(' ')))
    avg = (sum(l[1:])) / l[0]
    avg_over = [e for e in l[1:] if e > avg]
    rate = len(avg_over) / l[0] * 100
    print(f'{rate:.3f}%')