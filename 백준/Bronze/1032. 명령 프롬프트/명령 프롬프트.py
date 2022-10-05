n = int(input())
s_list = [input() for _ in range(n)]
temp = list(s_list[0])
for e in s_list[1:]:
    for i in range(len(e)):
        if temp[i] != e[i]:
            temp[i] = '?'
print(''.join(temp))