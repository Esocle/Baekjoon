n = int(input())
people = [input() for _ in range(n)]
people.sort()
res = ''
for i in range(n-4):
    if people[i][0] not in res and people[i][0] == people[i+4][0]:
        res += people[i][0]
if res == '':
    print('PREDAJA')
else:
    print(res)