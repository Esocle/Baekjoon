n = int(input())
s_list = [input() for _ in range(n)]
answer = list(s_list[0])
for e in s_list[1:]:
    for i in range(len(e)):
        if answer[i] != e[i]:
            answer[i] = '?'
print(''.join(answer))