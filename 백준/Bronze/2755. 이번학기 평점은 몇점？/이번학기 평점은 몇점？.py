
def new_round(n):
    n *= 100
    return (int(n)+1)/100 if (n - int(n)) >= 0.5 else int(n)/100

n = int(input())
score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
temp = [input().split() for _ in range(n)]
ans = 0
m = 0
for i in range(len(temp)):
        ans += score[temp[i][2]] * int(temp[i][1])
        m += int(temp[i][1])
print(f'{new_round(ans/m):.2f}')