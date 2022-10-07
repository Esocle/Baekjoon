num_list = list(input().split(' '))

for i in range(len(num_list)):
    num_list[i] = num_list[i][::-1]
    num_list[i] = int(num_list[i])
print(max(num_list))