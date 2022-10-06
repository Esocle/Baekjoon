s_list = list(input().split(' '))
if s_list[0] == '':
    del s_list[0]
if s_list[-1] == '':
    del s_list[-1]
print(len(s_list))