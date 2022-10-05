s = input().upper()
s_list = list(set(s))

cnt = []
for e in s_list:
    cnt.append(s.count(e))
max_num = max(cnt)
if cnt.count(max_num) != 1:
    print('?')
else:
    print(s_list[cnt.index(max_num)])