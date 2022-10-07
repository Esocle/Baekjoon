s_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for e in s_list:
    s = s.replace(e, 'x')
print(len(s))